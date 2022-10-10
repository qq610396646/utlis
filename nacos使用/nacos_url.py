# -*- coding: utf-8 -*-
"""
@Time ： 2022/9/13 10:08
@Auth ： CC
@File ：Nacos_Url.py
@IDE ：PyCharm
@Motto：Talk is cheap. Show me the code.

"""
import json
import requests
import yaml


class Nacos_Url_Class():

    def __init__(self, server_addresses):
        self.base_url = server_addresses

    def get_namespace(self,namespace_showname):
        url = self.base_url+"/nacos/v1/console/namespaces"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                namespace_list=json.loads(response.text)
                namespace = None
                if namespace_list["data"]:
                    for ns_dict in namespace_list["data"]:
                        if ns_dict["namespaceShowName"] == namespace_showname:
                            namespace = ns_dict["namespace"]
                            return namespace
                    if namespace is None:
                        raise KeyError(f"没有发现{namespace_showname}对应的命名空间ID")
                else:
                    raise AttributeError(f"namespace空间列表为空")
            else:
                print( f"code:{response.status_code},msg:{response.text}")
                return None
        except Exception as e:
            raise f"error:{e}"


    def get_config(self, namespace, dataId, group):

        url = self.base_url + "/nacos/v1/cs/configs"
        params = {"tenant": namespace, "dataId": dataId, "group": group}
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                yaml_config = yaml.load(response.text, Loader=yaml.FullLoader)
                print("load config success!")
                return yaml_config
            else:
                print( f"code:{response.status_code},msg:{response.text}")
                return None
        except Exception as e:
            raise f"error:{e}"

    def register_instance(self,
                          ip,
                          port,
                          namespaceId,
                          weight,
                          enabled,
                          healthy,
                          metadata,
                          serviceName,
                          clusterName="DEFAULT",
                          groupName="DEFAULT_GROUP",
                          ephemeral=True):

        url = self.base_url + "/nacos/v1/ns/instance"
        params = {
            "ip": ip,
            "port": port,
            "namespaceId": namespaceId,
            "weight": weight,
            "enabled": enabled,
            "healthy": healthy,
            "metadata": metadata,
            "serviceName": serviceName,
            "clusterName": clusterName,
            "groupName": groupName,
            "ephemeral": ephemeral,
            "encoding": "GBK"
        }
        try:
            response = requests.post(url, data=params)
            if response.status_code == 200:
                print("register instance success")
                return response.text
            else:
                return f"code:{response.status_code},msg:{response.text}"
        except Exception as e:
            return f"error:{e}"

    def delete_instance(self,
                        ip,
                        port,
                        namespaceId,
                        serviceName,
                        clusterName="DEFAULT",
                        groupName="DEFAULT_GROUP",
                        ephemeral=True):

        url = self.base_url + "/nacos/v1/ns/instance"
        params = {
            "ip": ip,
            "port": port,
            "namespaceId": namespaceId,
            "serviceName": serviceName,
            "clusterName": clusterName,
            "groupName": groupName,
            "ephemeral": ephemeral,
            "encoding": "GBK"
        }
        try:
            response = requests.delete(url, data=params)
            if response.status_code == 200:
                print("delete instant success!")
                return response.text
            else:
                print(f"code:{response.status_code},msg:{response.text}")
                return None
        except Exception as e:
            raise f"error:{e}"

    def search_instance(self,
                        namespaceId,
                        serviceName,
                        clusters="DEFAULT",
                        groupName="DEFAULT_GROUP",
                        healthyOnly=True):

        url = self.base_url + "/nacos/v1/ns/instance/list"
        params = {
            "namespaceId": namespaceId,
            "serviceName": serviceName,
            "clusters": clusters,
            "groupName": groupName,
            "healthyOnly": healthyOnly
        }
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return json.loads(response.text)
            else:
                print(f"code:{response.status_code},msg:{response.text}"),
                return None
        except Exception as e:
            raise f"error:{e}"

    def send_beat(self,
                  ip,
                  port,
                  namespaceId,
                  serviceName,
                  clusterName="DEFAULT",
                  groupName="DEFAULT_GROUP",
                  beat="",
                  ephemeral=True):
        url = self.base_url + "/nacos/v1/ns/instance/beat"
        params = {
            "ip": ip,
            "port": port,
            "namespaceId": namespaceId,
            "serviceName": serviceName,
            "clusterName": clusterName,
            "groupName": groupName,
            "beat": beat,
            "ephemeral": ephemeral
        }
        try:
            response = requests.put(url, data=params)
            if response.status_code == 200:
                # print("send beat success!")
                return response.text
            else:
                print(f"code:{response.status_code},msg:{response.text}")
                return None
        except Exception as e:
            raise f"error:{e}"

    def register_server(self,
                        namespaceId,
                        serviceName,
                        clusterName="DEFAULT",
                        groupName="DEFAULT_GROUP",
                        protectThreshold=0,
                        metadata="",
                        selector=""):
        url = self.base_url + "/nacos/v1/ns/service"
        params = {
            "namespaceId": namespaceId,
            "serviceName": serviceName,
            "clusterName": clusterName,
            "groupName": groupName,
            "protectThreshold": protectThreshold,
            "metadata": metadata,
            "selector": selector
        }
        try:
            response = requests.post(url, data=params)
            if response.status_code == 200:
                print("register service success!")
                return response.text
            else:
                print(f"code:{response.status_code},msg:{response.text}")
                return None
        except Exception as e:
            raise f"error:{e}"

    def delete_server(self,
                      namespaceId,
                      serviceName,
                      clusterName="DEFAULT",
                      ):
        url = self.base_url + "/nacos/v1/ns/service"
        params = {
            "namespaceId": namespaceId,
            "serviceName": serviceName,
            "clusterName": clusterName,
        }
        try:
            response = requests.delete(url, data=params)
            if response.status_code == 200:
                print("delete service success!")
                return response.text
            else:
                print(f"code:{response.status_code},msg:{response.text}")
                return None
        except Exception as e:
            raise f"error:{e}"

    def search_server(self,
                      namespaceId,
                      serviceName,
                      groupName="DEFAULT_GROUP",
                      ):
        url = self.base_url + "/nacos/v1/ns/service"
        params = {
            "serviceName": serviceName,
            "namespaceId": namespaceId,
            "groupName": groupName,
        }
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.text
            else:
                print(f"code:{response.status_code},msg:{response.text}")
                return None
        except Exception as e:
            raise f"error:{e}"
