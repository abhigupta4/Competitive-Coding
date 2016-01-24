#include <iostream>
#include <algorithm>

using namespace std;

int partition(long long int arr[],int low,int high){
    int x = arr[high];
    int temp = low - 1;
    for(int j = low;j <= high - 1;j++){
        if(arr[j] <= x){
            temp++;
            swap(arr[temp],arr[j]);
        }
    }
    swap(arr[temp + 1],arr[high]);
    return temp + 1;
}

void quicksort(long long int arr[],int low,int high){
    if(low < high){
        int parti = partition(arr,low,high);
        quicksort(arr,low,parti - 1);
        quicksort(arr,parti + 1,high);
    }
}

int binary_search(long long int arr[],int low,int high,int val){
    int mid;
    while(low <= high){
        if(low == high && arr[low] > val){
            return low;
        }
        mid = (low + high)/2;
        if(arr[mid] == val){
            int temp = mid + 1;
            while(temp <= high){
                if(arr[temp] > val){
                    return temp;
                }
                temp++;
            }
            return -1;
        }
        if(arr[mid] < val){
            low = mid + 1;
        }
        if(arr[mid] > val){
            high = mid;
        }
    }
    return -1;
}

int main() {
    int N,i,j;
    long long int count;
    while(1){
        cin >> N;
        if (N == 0){
            break;
        }
        long long int arr[N];
        for(i = 0;i < N;i++){
            cin >> arr[i];
        }
        quicksort(arr,0,N -1);
        count = 0;
        for(i = 0;i < N - 2;i++){
            for(j = i + 1;j < N - 1;j++){
                int temp = arr[j] + arr[i];
                int bin;
                bin = binary_search(arr,j + 1,N - 1,temp);
                //cout << bin << " ";
                if(bin != -1){
                    count += N - bin; 
                }
            }
        }
        cout << count << endl;
    }
    return 0;
}

//DONE