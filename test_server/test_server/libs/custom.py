from rest_framework import serializers

from rest_framework.exceptions import APIException


from rest_framework.response import Response


class DataResponse(Response):
    def __init__(self, data=None, status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None,success=None,message=None):
        ret = {'status':success,'message':message,'data':data}
        super().__init__(data=ret,status=status,template_name=template_name,headers=headers,exception=exception,content_type=content_type)


class NotFound(APIException):
    status_code = 404
    default_detail = '没有这个对象.'
    default_code = 'not found'

# class ResponseSerializer(serializers.ModelSerializer):
#     # def to_representation(self, instance):
#     #     ret = super(ResponseSerializer, self).to_representation(instance)
#     #     return {
#     #         'status':'ok',
#     #         'msg':'',
#     #         'data':ret
#     #     }
#     @property
#     def data(self):
#         ret = super().data()
#         return {
#             'status': 'ok',
#             'msg': '',
#             'data': ret
#         }