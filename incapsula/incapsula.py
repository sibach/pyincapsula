#!/usr/bin/python

import os
import requests

api_endpoint='https://my.incapsula.com/api/'

'''
def addSite
'''

def getSiteStatus(site_id, api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    url=api_endpoint + 'prov/v1/sites/status'
    payload={'api_id': api_id,'api_key': api_key, 'site_id': site_id}
    r = requests.post(url, data=payload)
    return r.text

'''
def getDomainApproverEmail
'''

'''
def modSiteConfig
'''

'''
def modSiteLogLevel
'''

'''
def modSiteSecurityConfig
'''

def modSiteACL(site_id, rule_id, listed, api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    if rule_id == 'api.acl.blacklisted_countries':
        payload={'api_id': api_id,'api_key': api_key, 'site_id': site_id, 'rule_id': rule_id, 'countries': listed}
    if rule_id == 'api.acl.blacklisted_urls':
        payload={'api_id': api_id,'api_key': api_key, 'site_id': site_id, 'rule_id': rule_id, 'urls': listed}
    if rule_id == 'api.acl.blacklisted_ips':
        payload={'api_id': api_id,'api_key': api_key, 'site_id': site_id, 'rule_id': rule_id, 'ips': listed}
    if rule_id == 'api.acl.whitelisted_ips':
        payload={'api_id': api_id,'api_key': api_key, 'site_id': site_id, 'rule_id': rule_id, 'ips': listed}
    url=api_endpoint + 'prov/v1/sites/configure/acl'
    r = requests.post(url, data=payload)
    return r.text

'''
def modWhitelistConfig
'''

'''
def delSite
'''

def listSites(api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    url=api_endpoint + 'prov/v1/sites/list'
    payload={'api_id': api_id,'api_key': api_key}
    r = requests.post(url, data=payload)
    return r.text

'''
def getSiteReport
'''

def purgeSiteCache(site_id, purge_pattern=None, api_id=os.environ.get('API_ID'), api_key=os.environ.get('API_KEY')):
    if purge_pattern:
        payload={'api_id': api_id,'api_key': api_key, 'site_id': site_id, 'purge_pattern': purge_pattern}
    else:
        payload={'api_id': api_id,'api_key': api_key, 'site_id': site_id}
    url=api_endpoint + 'prov/v1/sites/cache/purge'
    r = requests.post(url, payload)
    return r.text
    
'''
def modCacheMode
'''

'''
def getStats
'''

'''
def getVisits
'''

'''
def uploadPubKey
'''

'''
def changeLogCollectorStatus
'''

'''
def addLoginProtectUser
'''

'''
def editLoginProtectUser
'''

'''
def getLoginProtectUsers
'''

'''
def rmLoginProtectUser
'''

'''
def sendSMStoUser
'''

'''
def modSiteLoginProtectConfig
'''

'''
def configLoginProtectOnAdmin
'''

'''
def getIPRanges
'''

'''
def getTexts
'''

'''
def getGeoInfo
'''

'''
def getClientAppInfo
'''
