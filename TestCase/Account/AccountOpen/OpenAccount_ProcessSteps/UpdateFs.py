import requests

from Business.IdentityInformation import fsWorkStatus, fsCompanyName, fsWorkDesc, fsPost, fsPostOther, fsIndustry, \
    fsIndustryOther, fsWealthSource, fsWealthSourceOther, fsFundSource, fsFundSourceOther, fsTotalAssets, fsIncome, \
    fsRisk
from Business.OpenAccount_conmmonPath import path_update_fs
from Common.get_payload_headers import get_payload

from glo import HTTP


def UpdateFs(headers):
    """财务状况

    :param headers: 请求头headers（带token）
    :return:
    """
    url_update_fs = HTTP + path_update_fs
    if fsWorkStatus == 1 or fsWorkStatus == 2:
        fsWorkStatus1 = fsWorkStatus
        fsCompanyName1 = fsCompanyName
        fsWorkDesc1 = None
    else:
        if fsWorkStatus == 5:
            fsWorkStatus1 = 5
            fsWorkDesc1 = fsWorkDesc
            fsCompanyName1 = None
        else:
            fsWorkStatus1 = fsWorkStatus
            fsWorkDesc1 = fsWorkDesc
            fsCompanyName1 = None
    if fsPost == 6:
        fsPost1 = 6
        fsPostOther1 = fsPostOther
    else:
        fsPost1 = fsPost
        fsPostOther1 = fsPostOther
    if fsIndustry == 6:
        fsIndustry1 = 6
        fsIndustryOther1 = fsIndustryOther
    else:
        fsIndustry1 = fsIndustry
        fsIndustryOther1 = fsIndustryOther
    if fsWealthSource == 6:
        fsWealthSource1 = fsWealthSource
        fsWealthSourceOther1 = fsWealthSourceOther
    else:
        fsWealthSource1 = fsWealthSource
        fsWealthSourceOther1 = fsWealthSourceOther
    if fsFundSource == 4:
        fsFundSource1 = fsFundSource
        fsFundSourceOther1 = fsFundSourceOther
    else:
        fsFundSource1 = fsFundSource
        fsFundSourceOther1 = fsFundSourceOther

    paylo_update_fs = {
        "fsWorkStatus": fsWorkStatus1,
        "fsWorkDesc": fsWorkDesc1,
        "fsCompanyName": fsCompanyName1,
        "fsPost": fsPost1,
        "fsPostOther": fsPostOther1,
        "fsTotalAssets": fsTotalAssets,
        "fsIndustry": fsIndustry1,
        "fsIndustryOther": fsIndustryOther1,
        "fsIncome": fsIncome,
        "fsRisk": fsRisk,
        "fsWealthSource": fsWealthSource1,
        "fsWealthSourceOther": fsWealthSourceOther1,
        "fsFundSource": fsFundSource1,
        "fsFundSourceOther": fsFundSourceOther1
    }

    payload_update_fs = get_payload(paylo_update_fs)

    r_update_fs = requests.session().post(
        url=url_update_fs, headers=headers, data=payload_update_fs
    )
    return r_update_fs.json()
