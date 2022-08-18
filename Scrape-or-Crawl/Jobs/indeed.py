# Picked up from the cool developer - John Watson Rooney (Channel: https://www.youtube.com/c/JohnWatsonRooney)
# To be studied further.
from requests_html import HTMLSession
import csv


def job_data_get(s, url: str) -> tuple:
    # return the elements for each job card
    r = s.get(url)
    return r.html.find('ul.pagination-list a[aria-label=Next]'), r.html.find('div.job_seen_beacon')


def parse_html(job, url) -> dict:
    job_dict = {'title': job.find('h2 > a')[0].text,
                'link': url+'/viewjob?jk=' + job.find('h2 > a')[0].attrs['data-jk'],
                'companyname': job.find('span.companyName')[0].text,
                'snippet': job.find('div.job-snippet')[0].text.replace('\n', '').strip()}

    try:
        job_dict['salary'] = job.find('div.metadata.salary-snippet-container')[0].text
    except IndexError as err:
        job_dict['salary'] = 'no salary info'

    return job_dict


def export(results):
    keys = results[0].keys()
    with open('results.csv', 'w') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)


def main(baseurl, location):
    # Example baseurl = 'https://uk.indeed.com'

    job_search = 'python'

    s = HTMLSession()
    results = []
    url = baseurl + f'/jobs?q={job_search}&l={location}'
    while True:
        jobs = job_data_get(s, url)
        for job in jobs[1]:
            results.append(parse_html(job, url=baseurl))
        try:
            url = baseurl + jobs[0][0].attrs['href']
            print(url)
        except IndexError as err:
            print(err)
            break
    export(results)
