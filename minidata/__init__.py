"""Top-level package for minidata."""
from meutils.pipe import *

__author__ = """minidata"""
__email__ = 'yuanjie@xiaomi.com'
__version__ = '0.0'  # time.strftime("%Y.%m.%d.%H.%M.%S", time.localtime())

DATA_HOME = Path(get_module_path('data', __file__))
MODEL_HOME = Path(get_module_path('model', __file__))


class GoldenDataset(object):
    """ft格式
    大数据集链接
    小数据集打包
    """

    def __init__(self, data='同花顺相似问'):
        self._paths = list(DATA_HOME.rglob(f'*{data}*.ft'))

        logger.info(self._paths | xmap(lambda x: x.name) | xlist)

        if self._paths:
            self.dataframe = pd.read_feather(self._paths[0])


if __name__ == '__main__':
    # from transformers import AutoModel, AutoTokenizer, AutoConfig, AdamW
    #
    # PRE_TRAINED_MODEL_NAME = 'ckiplab/albert-tiny-chinese'
    #
    # tokenizer = AutoTokenizer.from_pretrained(MODEL_HOME / PRE_TRAINED_MODEL_NAME)
    #
    # print(tokenizer)

    NAME = '同花顺相似问'
    NAME = '蚂蚁金服相似问'
    NAME = '微众银行智能客服相似问'
    NAME = '情感分析/携程酒店评论'
    NAME = '敏感词'
    NAME = '字段'

    df = GoldenDataset(NAME).dataframe
    print(df)
