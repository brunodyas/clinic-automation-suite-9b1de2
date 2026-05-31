from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/6', tags=['feature'])

@router.get('/status')
def feature_6_status():
    return {'ok': True, 'feature': 'Implementar sistema de feedback dos pacientes', 'task': '6'}
