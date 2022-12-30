#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <semaphore.h>
#include <assert.h>
#include <time.h>

void set_color_to_red();
void set_color_to_green();
void set_color_to_default();
void set_color_to_yellow();
void set_color_to_blue();
sem_t semaphore;
int no_of_washing_machines;
int no_of_students;
int *T, *W, *P;
int no_of_students_who_could_not_wash = 0;
time_t total_time_wasted = 0;

pthread_mutex_t mutex;

void* routine(void* args) {
    time_t start = time(NULL);
    sleep(T[*(int*)args]);
    set_color_to_default();
    printf("%ld: Student %d arrives\n", (time(NULL)-start), *(int*)args+1);
    time_t arrival_time = (time(NULL)-start);
    struct timespec ts;
    clock_gettime(CLOCK_REALTIME, &ts);
    ts.tv_sec += P[*(int*)args];
    // a buffer of 0.1 seconds is added to the time to account for the time taken by the system to execute the intermediate instructions/code
    ts.tv_nsec += 100000000;
    if(!sem_timedwait(&semaphore, &ts)) {
        set_color_to_green();
        printf("%ld: Student %d starts washing clothes\n", (time(NULL)-start), *(int*)args+1);
        time_t time_wasted = (time(NULL)-start) - arrival_time;
        /* Uncomment the below code to find the time wasted by the individual students */
        // set_color_to_blue();
        // printf("Student %d wasted %ld seconds\n", *(int*)args+1, time_wasted);
        pthread_mutex_lock(&mutex);
        total_time_wasted += time_wasted;
        pthread_mutex_unlock(&mutex);
        sleep(W[*(int*)args]);
        set_color_to_yellow();
        printf("%ld: Student %d finishes washing clothes\n", (time(NULL)-start), *(int*)args+1);
        set_color_to_default();
        sem_post(&semaphore);
    } else {
        set_color_to_red();
        printf("%ld: Student %d leaves without washing\n", (time(NULL)-start), *(int*)args+1);
        time_t time_wasted = (time(NULL)-start) - arrival_time;
        /* Uncomment the below code to find the time wasted by the individual students */
        // set_color_to_blue();
        // printf("Student %d wasted %ld seconds\n", *(int*)args+1, time_wasted);
        pthread_mutex_lock(&mutex);
        total_time_wasted += time_wasted;
        pthread_mutex_unlock(&mutex);
        no_of_students_who_could_not_wash++;
        set_color_to_default();
    }
    free(args);
}

int main(int argc, char *argv[]) {
    pthread_mutex_init(&mutex, NULL);
    // input no of students and washing machines
    scanf("%d %d", &no_of_students, &no_of_washing_machines);
    // input T, W, P
    T = (int*)malloc(no_of_students * sizeof(int));
    W = (int*)malloc(no_of_students * sizeof(int));
    P = (int*)malloc(no_of_students * sizeof(int));
    for (int i = 0; i < no_of_students; i++) {
        scanf("%d %d %d", &T[i], &W[i], &P[i]);
    }
    pthread_t th[no_of_students];
    sem_init(&semaphore, 0, no_of_washing_machines);
    int i;
    for (i = 0; i < no_of_students; i++) {
        int* a = malloc(sizeof(int));
        *a = i;
        if (pthread_create(&th[i], NULL, &routine, a) != 0) {
            perror("Failed to create thread");
        }
    }

    for (i = 0; i < no_of_students; i++) {
        if (pthread_join(th[i], NULL) != 0) {
            perror("Failed to join thread");
        }
    }
    sem_destroy(&semaphore);
    pthread_mutex_destroy(&mutex);
    printf("%d\n", no_of_students_who_could_not_wash);
    printf("%ld\n", total_time_wasted);
    if (((float) no_of_students_who_could_not_wash/(float)no_of_students) >= 0.25) {
        printf("Yes");
    }
    else{
        printf("No");
    }
    return 0;
}

void set_color_to_red(){
    printf("\033[1;31m");
}

void set_color_to_green(){
    printf("\033[0;32m");
}

void set_color_to_default(){
    printf("\033[0m");
}

void set_color_to_yellow(){
    printf("\033[1;33m");
}

void set_color_to_blue(){
    printf("\033[0;34m");
}

/*
Test Case 1:
5 2
6 3 5
3 4 3
6 5 2
2 9 6
8 5 2

Test Case 2:
3 1
2 5 1
1 2 4
2 4 2
*/