from .models import USPTO_all
from .serializers import allSerializer, partSerializer
from . import pagination

from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import get,query_set_all

class ListAPIView(APIView):
    name = 'api_list'

    def get(self, request):
        """查询多条数据"""
        # 1. 实例化分页器对象
        page_obj = pagination.PageNumberPagination()
        # 2. 使用自己配置的分页器调用分页方法进行分页
        page_data = page_obj.paginate_queryset(query_set_all, request)
        # 3. 序列化我们分页好的数据
        serializer = partSerializer(page_data, many=True)
        # 返回响应对应
        return page_obj.get_paginated_response(serializer.data)

    def post(self, request):
        """新增一条数据"""
        # 创建序列化对象
        serializer = partSerializer(data=request.data)
        # 验证参数合法性
        # 设置raise_exception=True后，出错时，会给客户端返回json出错信息
        serializer.is_valid(raise_exception=True)
        # 保存部门到数据库表中
        serializer.save()
        # 返回响应对象
        return Response(serializer.data)


class DetailAPIView(APIView):
    name = 'api_detail'

    def get(self, request, pk):
        """查询一条数据"""
        try:
            data = USPTO_all.objects.get(pk=pk)
        except:
            return Response(status=404)
        # 创建序列化对象
        serializer = allSerializer(data)
        # 返回响应对象，并传递字典数据
        return Response(serializer.data)

    def put(self, request, pk):
        """修改"""
        try:
            data = USPTO_all.objects.get(_id=pk)
        except:
            return Response(status=404)
        # 创建序列化器对象
        serializer = allSerializer(data, data=request.data)
        # 验证参数合法性
        # raise_exception=True: 如果校验不通过，会返回json出错信息给客户端
        serializer.is_valid(raise_exception=True)
        # 保存数据到数据库中
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        # 删除
        try:
            data = USPTO_all.objects.get(_id=pk)
        except:
            return Response(status=404)
        # 删除
        data.delete()
        # 响应请求
        return Response(status=204)


###substruct
class ListSubstruct(APIView):
    name = 'api_substruct'

    def get(self, request):
        """查询子结构数据"""
        ss_mol = get(request.GET['smiles'])
        hit=[]
        for i, reaction_smiles in enumerate(query_set_all):
            reaction_smiles = str(reaction_smiles).split(' ')[0]
            products = [get(x) for x in reaction_smiles.split('>')[2].split('.')]
            reactants = [get(x) for x in reaction_smiles.split('>')[0].split('.')]
            for mol in reactants+products:
                if mol.HasSubstructMatch(ss_mol):
                    hit.append(i)
                    break

        query_set = USPTO_all.objects.filter(pk__in=hit)
        # 1. 实例化分页器对象
        page_obj = pagination.PageNumberPagination()
        # 2. 使用自己配置的分页器调用分页方法进行分页
        page_data = page_obj.paginate_queryset(query_set, request)
        # 3. 序列化我们分页好的数据
        serializer = partSerializer(page_data, many=True)
        # 返回响应对应
        return page_obj.get_paginated_response(serializer.data)
