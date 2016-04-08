# -*- coding:utf-8 -*-
# from
from flask import Flask,render_template,request
import json
import simplejson
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append("./wordCloud/")
sys.path.append("./wordCloud/data/")
sys.path.append("./wordCloud/text_rank_model/")
from rank_write_mongo import get_wordcloud_data


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/wordcloud/')
@app.route('/wordcloud/<data>')
def wordcloud(data=None):
    # params = request.args.items()
    data = None
    brand = request.args.get('brand')
    stime = request.args.get('stime')
    etime = request.args.get('etime')
    source = request.args.get('source')
    if brand is not None and stime is not None and etime is not None and source is not None:
        data = get_wordcloud_data(stime, etime, brand, source)
        # data = [{u'\u6ca1\u6709': 120}, {u'\u4ef7\u683c': 97}, {u'\u77e5\u9053': 91}, {u'\u5927\u5bb6': 85}, {u'\u95ee\u9898': 70}, {u'\u611f\u89c9': 64}, {u'\u58f0\u97f3': 51}, {u'\u8f6e\u6bc2': 51}, {u'\u53d1\u52a8\u673a': 49}, {u'\u4fdd\u517b': 48}, {u'\u5927\u795e': 48}, {u'\u8bf7\u95ee': 47}, {u'\u9700\u8981': 46}, {u'\u5ea7\u6905': 46}, {u'\u63d0\u8f66': 44}, {u'\u6709\u6ca1\u6709': 44}, {u'\u673a\u6cb9': 43}, {u'\u60c5\u51b5': 42}, {u'\u914d\u7f6e': 40}, {u'\u670b\u53cb': 38}, {u'\u81ea\u52a8': 38}, {u'\u9500\u552e': 37}, {u'\u89c9\u5f97': 37}, {u'\u542f\u52a8': 37}, {u'\u6709\u70b9': 36}, {u'\u5185\u9970': 36}, {u'\u5239\u8f66': 36}, {u'\u53d1\u73b0': 35}, {u'\u65b0\u6b3e': 33}, {u'\u770b\u770b': 33}, {u'\u53ef\u80fd': 33}, {u'\u8f66\u53cb': 33}, {u'\u5e94\u8be5': 32}, {u'\u4e0d\u4f1a': 31}, {u'4S\u5e97': 30}, {u'\u84dd\u7259': 29}, {u'\u539f\u5382': 29}, {u'\u5bfc\u822a': 29}, {u'\u597d\u50cf': 28}, {u'\u8f66\u5b50': 28}, {u'\u4f18\u60e0': 28}, {u'\u51c6\u5907': 28}, {u'\u8f6e\u80ce': 27}, {u'\u51fa\u6765': 26}, {u'\u52a0\u88c5': 26}, {u'\u65b9\u5411\u76d8': 26}, {u'\u8bba\u575b': 26}, {u'\u843d\u5730': 25}, {u'\u559c\u6b22': 24}, {u'\u4f30\u8ba1': 24}, {u'\u663e\u793a': 23}, {u'\u771f\u76ae': 23}, {u'\u5012\u8f66': 23}, {u'\u80af\u5b9a': 23}, {u'\u5f00\u8f66': 22}, {u'\u5927\u706f': 22}, {u'\u79c1\u4fe1': 22}, {u'\u513f\u5b50': 21}, {u'\u7535\u8bdd': 21}, {u'\u529f\u80fd': 21}, {u'4s\u5e97': 20}, {u'\u8d77\u6765': 20}, {u'\u94a5\u5319': 20}, {u'\u51fa\u73b0': 20}, {u'\u770b\u5230': 20}, {u'\u6cb9\u8017': 19}, {u'\u539f\u56e0': 19}, {u'\u9ed1\u8272': 19}, {u'\u6c7d\u8f66': 19}, {u'\u65b0\u8f66': 19}, {u'\u6392\u6c14': 19}, {u'\u884c\u9a76': 18}, {u'\u8d37\u6b3e': 18}, {u'\u53ea\u80fd': 18}, {u'\u540e\u89c6\u955c': 17}, {u'\u6280\u672f': 17}, {u'\u540e\u6392': 17}, {u'\u9047\u5230': 17}, {u'\u4fdd\u9669': 17}, {u'\u7ea0\u7ed3': 17}, {u'\u5f71\u50cf': 17}, {u'\u5165\u624b': 17}, {u'\u6539\u88c5': 17}, {u'\u65f6\u95f4': 17}, {u'\u767d\u8272': 16}, {u'\u5730\u65b9': 16}, {u'\u9009\u62e9': 16}, {u'\u53d8\u901f\u7bb1': 16}, {u'\u52a8\u529b': 16}, {u'\u66f4\u6362': 16}, {u'\u7184\u706b': 16}, {u'\u4e70\u8f66': 15}, {u'\u4e1c\u897f': 15}, {u'\u624b\u673a': 15}, {u'\u8f66\u4e3b': 15}, {u'\u4e0d\u5230': 15}, {u'\u6253\u5f00': 15}, {u'\u6309\u952e': 15}, {u'\u56fd\u4ea7': 15}, {u'\u6da1\u8f6e': 15}]

        data = simplejson.dumps(data["words"], encoding="UTF-8", ensure_ascii=False)
        # data = json.dumps(data["words"]).decode("unicode-escape")

        input = 'stime:' + stime +'   etime:' + etime +'   brand:' + brand +'   source:' + source
        return render_template('wordcloud.html', data=data, input=input)

    return render_template('wordcloud.html')
    # return {"param":request.args.get('abc')}

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)