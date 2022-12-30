int main(int argc, char *argv[])
{
    int priority, pid;
    if (argc != 3)
    {
        fprintf(2, "Wrong number of arguments\n");
        exit(1);
    }

    priority = atoi(argv[1]);
    pid = atoi(argv[2]);

    if (priority < 0 || priority > 100)
    {
        fprintf(2, "Invalid: Priority should range from 0 to 100\n");
        exit(1);
    }
    set_priority(priority, pid);
    exit(1);
}
