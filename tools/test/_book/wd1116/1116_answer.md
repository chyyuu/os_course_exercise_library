知识点：实验环境准备实验。
出处：网络
难度：1
大家熟悉了生产-消费问题(PC),这个问题很简单。题目较为新颖,但是本质非常 简单即:生产-消费问题的简化或者说是两个进程的简单同步问题。答案如下:
设信号量s1 和s2 分别表示可拣白子和黑子; 不失一般性,若令先拣白子。
    ```
    var S1 , S2 : semaphore;
    S1 : = l; S2 :=0;
    cobegin
      process P1           Process P2
       begin                begin
       repeat               repeat
       P(S1);               P(S2);
       pick The white;      pick the black;
       V(S2);               V(S1);
      until false ;         until false;
      end                   end
    coend
    ```
    
