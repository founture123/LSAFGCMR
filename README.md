# LSAFGCMR

train: 

  run main.py;
  
test: 

  run test.py to extra (image、audio、text) features; 
  
  run video_feature.py + video_feature_cal.py to extra video features ;
  
  run retrieval.py to get mAP scores;

pretrained model download:

  https://github.com/hszhao/SAN ;
  
trained model download:

  https://pan.baidu.com/s/1GlDbEbZizk5jncEwXlbpig;
  password: fwb8;
  
dataset download:
  
  https://www.wict.pku.edu.cn/mipl/ ;
