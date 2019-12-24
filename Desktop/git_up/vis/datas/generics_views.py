from pymongo import MongoClient  # mongodb plugin
from .models import USPTO_all
from .serializers import allSerializer, partSerializer
from .pagination import PageNumberPagination

#from rest_framework import generics
# 可能会用到这个generics
from rest_framework_mongoengine import generics

from .utils import get,query_set_all

def f():
    ### 先运行一遍存到cache里面。。。####
    for reaction_smiles in enumerate(query_set_all):
        reaction_smiles = str(reaction_smiles[1]).split(' ')[0]
        products = [get(x) for x in reaction_smiles.split('>')[2].split('.')]
        reactants = [get(x) for x in reaction_smiles.split('>')[0].split('.')] 
###################################
f()

class ListView(generics.ListAPIView):
    name = 'generics_list'

    def get_queryset(self):
        return query_set_all

    # 序列化设置
    serializer_class = partSerializer

    # 分页设置
    pagination_class = PageNumberPagination

    # def get_serializer_class(self):
    #     return partSerializer


class ListDetail(generics.ListAPIView):
    name = 'generics_detail'

    def get_queryset(self):  # self.kwargs['pk']
        pk = self.kwargs['pk']
        queryset = USPTO_all.objects(pk=pk)
        return queryset

    serializer_class = allSerializer


class ListSubstruct(generics.ListAPIView):
    name = 'generics_substruct'

    def get_queryset(self):
        # 获取get过来的对象。
        ss_mol=get(self.request.GET['smiles'])
        hit = []

        for i, reaction_smiles in enumerate(query_set_all):
            reaction_smiles = str(reaction_smiles).split(' ')[0]
            products = [get(x) for x in reaction_smiles.split('>')[2].split('.')]
            reactants = [get(x) for x in reaction_smiles.split('>')[0].split('.')]
            for mol in reactants+products:
                if mol.HasSubstructMatch(ss_mol):
                    hit.append(i)
                    break

        queryset = USPTO_all.objects.filter(pk__in=hit)

        return queryset

    serializer_class = partSerializer

    pagination_class = PageNumberPagination