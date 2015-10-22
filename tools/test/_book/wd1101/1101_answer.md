��
第二题： 一、 （10分）给出程序fork.c的输出结果。
注：1）getpid()和getppid()是两个系统调用，分别返回本进程标识和父进程标识。
2）你可以假定每次新进程创建时生成的进程标识是顺序加1得到的；在进程标识为1000的命令解释程序shell中启动该程序的执行
    ```
    nclude
    #include
    / getpid() and fork() are system calls declared in unistd.h.  They return /
    / values of type pid_t.  This pid_t is a special type for process ids. /
    / It's equivalent to int. /
    int main(void)
    {
      pid_t childpid;
      int x = 5;
            int i;
      childpid = fork();
      for ( i = 0;  i < 2;  i++)  {
        printf(This is process %d; childpid = %d; The parent of this process has id %d; i = %d; x = %d
"
getpid()
- [x]

知识点：。
出处：网络
难度：1
getppid()
