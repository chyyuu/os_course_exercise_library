把上一级目录中夹“1”至“15”内所有的 .md格式的文件转化为.json

.json文件的组织方式为：

   由以下6个字段组成：

      "type"：题目类型
      "question"：题干
      "options"：选项
      "answer"：参考答案
      "degree_of_difficulty"：难度
      "knowleget"：知识点
      
md2json.py:实现把.md格式转化为 .json  的python脚本（python2.7编译器）
