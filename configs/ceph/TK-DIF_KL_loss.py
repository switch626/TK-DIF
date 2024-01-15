_base_ = ['../../../../_base_/datasets/ceph.py']
log_level = 'INFO'
load_from = None
resume_from = None
dist_params = dict(backend='nccl')
workflow = [('train', 1)]
checkpoint_config = dict(interval=200)
evaluation = dict(interval=1, metric='NME', save_best='NME')
