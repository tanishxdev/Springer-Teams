from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from jobs.models import Job
from scans.models import ScanResult
from scans.services import run_fake_extraction


class ScanStartView(APIView):
    def post(self, request):
        job = Job.objects.create()
        run_fake_extraction(job.id)

        return Response(
            {
                "job_id": str(job.id),
                "status": job.status,
            },
            status=status.HTTP_202_ACCEPTED,
        )


class ScanStatusView(APIView):
    def get(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return Response(
                {"error": "Job not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            {
                "job_id": str(job.id),
                "status": job.status,
            }
        )


class ScanResultView(APIView):
    def get(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return Response({"error": "Job not found"}, status=404)

        if job.status != Job.Status.COMPLETED:
            return Response(
                {"error": "Job not completed"},
                status=409,
            )

        return Response(job.result.data)


class ScanCancelView(APIView):
    def post(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return Response({"error": "Job not found"}, status=404)

        if job.status in [Job.Status.COMPLETED, Job.Status.FAILED]:
            return Response(
                {"error": "Cannot cancel completed job"},
                status=409,
            )

        job.status = Job.Status.CANCELLED
        job.save()
        return Response({"status": "cancelled"})


class ScanRemoveView(APIView):
    def delete(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return Response({"error": "Job not found"}, status=404)

        job.delete()
        return Response(status=204)
