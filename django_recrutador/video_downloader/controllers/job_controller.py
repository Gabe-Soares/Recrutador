from ..services import job_service


def getJobs():
    jobs_list = job_service.getJobsList()
    return jobs_list


def addJob(name):
    job_service.createJob(name)
    return
