# README

## 逻辑
1. 判断是否过于激进的批评。
    - 对于过分激进的判定，决定使用azure service的sentiment analysis 来判定。sentiment analysis会对于一个text返回一个score来判定，这个score接近0就是更加负面情感，接近1就是更加正面情感。对于判定是“喷”还是常规性批评，则需要设定一个阈值，超过这个阈值则是喷，否则为批评。
    - 对于这个阈值，通过机器学习来判定。实验方法：获取正常的score< 0.5的tweet，与获取喷的score<0.5的tweet，进行划分。如果能够直观的划分，譬如能直观发现threshold < score < 0.5是正常批评，0 《 score < threshold 是喷，则可以直接判定threshold（如果中间有个较大的间隔，则可以使用一维svm的设定方法），如果没有，则1.使用线性划分2. 信息量不够，处理方法为将输入片段使用word2vec进行向量化，然后做线性回归。
2. 判断是否是阴阳怪气的评论。

    - 对于阴阳怪气的评论，即azure service的sentiment analysis评价的score>0.5但是却是喷子语气的。比如“@Breaking911 Build that wall!! 👍“这种阴阳怪气的话。这句话获得了1.0的高分，但是却是阴阳怪气的话。

    - 对于这种阴阳怪气的话，我使用3种方法

      1. 由于对一个人的价值观很难判断，于是我默认社会的价值观与舆论价值观相符合。大多数阴阳怪气都是基于梗的。意思是阴阳怪气的话的负面态度是基于背景故事和新闻时事。于是为了这些可以通过

         - urban dictionary的梗数据库，通过查找句子和句子中的entity来判断是否有负面梗来查看句子是不是阴阳怪气（有负面梗就是阴阳怪气）
         - Google News（https://news.google.com）可以查找entity和句子中的新闻人物和时事，根据网页中附有的Opinion和Analysis判断是不是阴阳怪气。如果Opinion和Analysis都是负面的，那么就可能是阴阳怪气。

      2. 对于一个人的态度需要通过他的历史发言来判断，可以通过爬取以前的tweet来判断态度。

         爬取使用者以前的推特，观察态度

         使用thread reader爬取

         使用twitter 官方api爬取

      3. 最后取上面的所有信息，使用lstm进行训练。

