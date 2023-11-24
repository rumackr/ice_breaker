import os

import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIN profiles,
    Manually scrape the information form the LinkedIn Profile"""

    headers = {'Authorization': f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    params = {
        'linkedin_profile_url': linkedin_profile_url,
    }
    response = requests.get(api_endpoint,
                            params=params,
                            headers=headers)
    ##for if you dont want to pay for the API calls
    # response = requests.get(
    #     "https://gist.githubusercontent.com/rumackr/824b69d7791cb0c0ded8b5b18190e8d8/raw/8b6c4d9b59e8287a21b6633b1c638b4f944c1397/reid_rumack.json")
    #
    data = response.json()
    if data.get("profile_pic_url") == None:
        data["profile_pic_url"] = "https://www.jobscan.co/wp-content/uploads/13-Brian-Murphey-_-LinkedIn.png"
    ## For limiting token ingest
    data = {
        k: v
        for k, v in data.items()
        # remove empty fields and Certifcations and people_also_viewed
        if v not in ([], "", "", None)
           and k not in ["people_also_viewed", "certifications", "accomplishment_courses"]
    }

    if data.get("groups"):
        # remove groups
        for group_dict in data.get("groups"):
            # remove profile pic urls
            group_dict.pop("profile_pic_url")

    return data