import os.path as osp
import basicsr
import odisr
# with torch.autograd.set_detect_anomaly(True)
import os
os.environ['CUDA_VISIBLE_DEVICES'] = "4"

if __name__ == '__main__':
    root_path = osp.abspath(osp.join(__file__, osp.pardir))
    
    basicsr.train_pipeline(root_path)
