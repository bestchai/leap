import sys
sys.path.append("../")
import api.leap as leap
import api.leap_fn as leap_fn
import api.codes as codes
import api.register.user.registration as user_reg

from proto import computation_msgs_pb2

def predef_count_selector():
    leap_predef = leap_fn.PredefinedFunction(computation_msgs_pb2.AlgoCodes.COUNT_ALGO)
    selector = {"type": "default", "filter": "[pain_past3backpain] = 1 and [yrbirth] < 1931"}
    leap_predef.selector = selector
    return leap_predef

def predef_count_selector_sql():
    leap_predef = leap_fn.PredefinedFunction(computation_msgs_pb2.AlgoCodes.COUNT_ALGO)
    selector = {"type": "sql", "sql_func": "count", "sql_options": {"project_id": 13, "filter" : {'pain_past3backpain': "= 1", 'yrbirth': "< 1931"}}}
    leap_predef.selector = selector
    return leap_predef

def distributed(sites, username):
    filter_fn = predef_count_selector_sql()
    dist_leap = leap.DistributedLeap(filter_fn, "127.0.0.1:50000", username)
    print("Count using REDCap's getData method with filters:")
    print(dist_leap.get_result(sites))


if __name__ == "__main__":
    user_reg.register_user("TestUser", "123456", "127.0.0.1:50000")
    distributed([1], "TestUser")