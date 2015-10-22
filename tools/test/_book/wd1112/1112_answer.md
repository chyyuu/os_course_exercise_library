知识点：。
出处：网络
难度：1
Code1： tf->tf_trapno Code 2: ret = pgfault_handler(tf) Code 3: page - pages;
Code 4: page2ppn(page) << PGSHIFT Code 5: page2pa(page) | PTE_P | perm;
\--------------------------------- 评分标准 5个空，每个3分； 第4个空中，对了前半部分，给2分；移位正确给1分；
第5个空中，每一个部分1分
