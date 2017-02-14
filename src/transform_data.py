from scipy.stats import zscore

def z_score(data):
  return zscore(data)
  #return (data - data.mean())/data.std()
