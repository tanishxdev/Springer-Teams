import threading
import time
from jobs.models import Job
from scans.models import ScanResult


def run_fake_extraction(job_id):
    def task():
        job = Job.objects.get(id=job_id)
        job.status = Job.Status.RUNNING
        job.save()

        time.sleep(5)

        ScanResult.objects.create(
            job=job,
            data={
                "records": [
                    {"email": "a@test.com"},
                    {"email": "b@test.com"},
                ]
            },
        )

        job.status = Job.Status.COMPLETED
        job.save()

    threading.Thread(target=task, daemon=True).start()
