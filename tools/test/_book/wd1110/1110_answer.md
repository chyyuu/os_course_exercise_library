知识点：实验环境准备实验。
出处：网络
难度：1
从井中取水并放入水缸是一个连续的动作可以视为一个进程,从缸中取水为另一 个进程。
设水井和水缸为临界资源,引入mutex1,mutex2;三个水桶无论从井中取水还是放
入水缸中都一次一个,应该给他们一个信号量count,抢不到水桶的进程只好为等待,
水缸满了时,不可以再放水了。设empty控制入水量,水缸空了时,不可取水设full。
    ```
    var mutex1,mutex2,empty,full,count:semaphore;
    mutex1:=mutex2:=1;
    empty:=10;
    full:=0;
    count:=3;
    cobegin
      Procedure Fetch_Water
        begin
         while true
          p(empty);
          P(count);
          P(mutex1);
           Get Water;
          v(mutex1);
          P(mutex2);
          pure water into the jar;
          v(mutex2);
          v(count);
          v(full);
        end
    coend
    Procedure Drink_Water
     begin
       while true
        p(full);
        p(count);
        p(mutex2);
          Get water and
          Drink water;
        p(mutex2);
        v(empty);
        v(count);
    end
    ```
    
