import datetime
import os
#token_expiry = datetime.datetime.fromisoformat("2023-12-18T13:31:14.695Z")
#datetime.datetime.fromisoformat
#token_expiry = datetime.datetime.strptime("2023-12-18T13:31:14.695Z", '%Y-%m-%d %H:%M:%S.%f')

date_str = "2023-12-18"
parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
print(parsed_date)

os.environ['CHANGE_SCOPE'] = 'True'
#os.environ['CHANGE_SCOPE'] = 'False'
#change_scope = os.environ.get('CHANGE_SCOPE', None)
# if change_scope == True:
#     print('inside')
# else:
#     print('outside')

if True == os.environ.get('CHANGE_SCOPE', None):
    print('inside')
else:
    print('outside')

#token = None
#if not token:
#    print("token credentials^portal_apitoken not exists in 'portal-dynatrace-key'")

class PostDeploy:

    @staticmethod
    def test1(a):
        print(a)
        dt_inst = {}
        #dt_inst = None
        #dt_inst = 'matan'
        dt_inst = {'type': 'managed'}
        if not dt_inst or dt_inst['type'] != 'managed':
            print('portal-dynatrace is not a managed service instance, skipping the process...')
            return
        
        print('*****************************')
        print('Dynatrace code is running!!!')
        print('*****************************')


first = "**** Hello"
second = " World ****"
PostDeploy.test1(first + second)

m = {'a': 1, 'b': 2}

c = m.get('c')
print(c)
print('******************************************')
env_map = {
            'APPLICATION_VERSION': 'version',
            'DYNATRACE_CUSTOM_METRICS_API_TOKEN': 'dynatrace_custom_metrics_api_token',
            'DT_CLUSTER_ID': 'cccccc',
            'DT_RELEASE_PRODUCT': 'app_name',
            'DT_RELEASE_STAGE': 'LANDSCAPE_NAME',
            'DT_RELEASE_BUILD_VERSION': 'vvvv',
            'DT_RELEASE_VERSION': 'SPRINT_NAME'
        }

env_map100 = {
            'APPLICATION_VERSION': 'version2',
            'DYNATRACE_CUSTOM_METRICS_API_TOKEN2': 'dynatrace_custom_metrics_api_token',
        }
#        md = benedict(self.deployment_descriptor, keypath_separator='^')
#        # set application env
#        md_env = md.get('applications[0]^env')
#        merged_env = {**(md_env if md_env else {}), **env_map}
#merged_env = {**{}, **env_map}
merged_env = {**env_map100, **env_map}
print(merged_env)
print('THE END')
