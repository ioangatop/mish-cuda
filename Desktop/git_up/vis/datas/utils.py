import rdkit.Chem as Chem
from functools import lru_cache
from fastcache import clru_cache
from .models import USPTO_all

@clru_cache(maxsize=None)
def get(smiles):
    mol = Chem.MolFromSmiles(smiles, sanitize=False)
    return mol


query_set_all = USPTO_all.objects.all()

