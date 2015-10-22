知识点：实验环境准备实验。
出处：网络
难度：1
在本题中,爸爸、儿子、女儿共用一个盘子,盘中一次只能放一个水果。当盘子为 空时,爸爸可将一个水果放入果盘中。若放入果盘中的是桔子,则允许儿子吃,女儿必
须等待;若放入果盘中的是苹果,则允许女儿吃,儿子必须等待。本题实际上是生产 者-消费者问题的一种变形。这里,生产者放入缓冲区的产品有两类,消费者也有两类,
每类消费者只消费其中固定的一类产品。
在本题中,应设置三个信号量S、So、Sa,信号量S表示盘子是否为空,其初值为l;
信号量So表示盘中是否有桔子,其初值为0;信号量Sa表示盘中是否有苹果,其初值为0。 同步描述如下:
    ```
    S=1; Sa=0; So=0;
    cobegin
     Procedure father;
     Procedure son;
     Procedure daughter;
    coend
    Procedure father:
      begin
      while(TRUE)
      begin
      P(S);
      将水果放入盘中;
      if(放入的是桔子)
      V(So);
      else
      V(Sa);
      end
      end
    Procedure son:
      begin
      while(TRUE)
      begin
      P(So);
      从盘中取出桔子;
      V(S);
      吃桔子;
      end
      end
    Procedure daughter:
      begin
      while(TRUE)
      begin
      P(Sa);
      从盘中取出苹果;
      V(S);
      吃苹果;
      end
    end
    ```
    
