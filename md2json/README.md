把上一级目录中夹“1”至“15”内所有的 .md格式的文件转化为.json

.json文件的组织方式为：

   由以下6个字段组成：

      "type"：题目类型
      "question"：题干
      "options"：选项
      "answer"：参考答案
      "degree_of_difficulty"：难度
      "knowlege"：知识点
      
md2json.py:实现把.md格式转化为 .json  的python脚本（python2.7编译器）

规范的.json文件格式：
    下面是一个示例：
    ```json
   {
      "type": "single_answer",
      "question": "关于段页式存储管理系统中的页表数，下面哪种说法比较准确？",
      "degree_of_difficulty": "1",
      "source": "网络", 
      "options": [
         " A.整个系统有一个 ",
         " B.整个系统有多个 ",
         " C.每个进程有一个 ",
         " D.每个进程有多个"
      ],
      "knowledge": "非连续内存分配。"
      }
    ```
   type:有四种类型，(单选题："single_answer"),(多选题："multi_answer")，填空题：，问答题，判断题：
