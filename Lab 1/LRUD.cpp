#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
using namespace std;


int alm = 1;
int vari = 0;

struct position 
{
    int data, depth;
    position* parent;
    bool visited;
    position() 
    {
        parent = NULL;
        visited = false;
        depth = 99999;
    }
};
struct adj 
{
    vector<position*> arr;
    void disp() 
    {
        for(int i = 0; i<arr.size() ;i++) 
        {
            cout << arr[i]->data << " ";
        }
        cout << endl;
    }
};

void dfid(position* start, adj* adj_list, int depth, int dest, position* node) 
{
    if(start->depth < depth) 
    {
        start->visited = true;
        if (start->data == dest) 
        {
            vari = alm;
        }
        alm++;
        for(int i = 0;i < adj_list[start->data].arr.size();i++) 
        {
            if((adj_list[start->data].arr[i]->depth > start->depth + 1)) 
            {
                adj_list[start->data].arr[i]->parent = start;
                adj_list[start->data].arr[i]->depth = start->depth + 1;

                dfid(adj_list[start->data].arr[i],adj_list,depth,dest,node);
            }
        }
    }
    return;
}

int main()
{

    int source = 0;
    int dest;
    int length = 1;

    ifstream fin;
    string file;
    cout << "enter file name: ";
    cin >> file;

    // cout<< file;

    fin.open(file);
    vector<string> maze;
    string str;

    getline(fin,str);
    
    int option=stoi(str);

    while(getline(fin,str)) 
    {
        maze.push_back(str);
    }

    int m1 = maze.size();
    int n1 = maze[0].length();

    position node[99999];
    adj adj_list[99999];

    for(int i = 0;i < maze.size();i++) 
    {
        for(int j = 0;j < maze[i].size();j++) 
        {
            int pos = n1*i + j;
            node[pos].data = pos;
            if(maze[i][j] == '*') dest = pos;
            if(maze[i][j] == ' ' or ( i == 0 && j == 0)) 
            {
                if(j > 0 && (maze[i][j-1] == ' ' or maze[i][j-1] == '*')) adj_list[pos].arr.push_back(&node[pos - 1]);
                if(j < n1 && (maze[i][j+1] == ' ' or maze[i][j+1] == '*')) adj_list[pos].arr.push_back(&node[pos + 1]);
                if(i > 0 && (maze[i-1][j] == ' ' or maze[i-1][j] == '*')) adj_list[pos].arr.push_back(&node[pos - n1]);
                if(i < m1 && (maze[i+1][j] == ' ' or maze[i+1][j] == '*')) adj_list[pos].arr.push_back(&node[pos + n1]);
            }
        }
    }

    //cout<<str<<endl;
    //cout<<option<<endl;
    string s;
    getline(fin,str);
    while(getline(fin,s)){ 
        //cout<<s<<endl;
       // cout<<s.length()<<endl;
       // cout<<s[13];
        //cout<<s[0]<<endl;
        maze.push_back(s);
    }
    int n=maze.size();
   // cout<<n<<endl;
    int p=maze[0].size();
    //cout<<maze[0];
    //cout<<m<<endl;
    int m=p-0;
    char value[n*(m)];
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            value[m*i+j]=maze[i][j];
        }
    }
    int parent[n*m]={0};
        int visited[n*m]={0};
        parent[0]= -1;
       
        vector<int> closed;
        
        visited[0]==1;
        int fron;
        int state=0;

    



    if(option==0)
    {
         queue<int> open;
         open.push(0);

        while(!open.empty()){
            fron=open.front();
            // cout<<fron<<endl;
            if(value[fron]=='*'){
                state++;
                break;
            }
            if(fron%m==0){
                if(fron==0){
                    if(value[fron+m]==' '|| value[fron+m]=='*'){
                         if(visited[fron+m]==0){
                            open.push(fron+m);
                            parent[fron+m]=fron;
                            visited[fron+m]=1;
                        }
                    }
                    if(value[fron+1]==' '|| value[fron+1]=='*'){
                         if(visited[fron+1]==0){
                            open.push(fron+1);
                            parent[fron+1]=fron;
                            visited[fron+1]=1;
                        }
                    }
                }
                else if(fron==(m*(n-1))){
                     if(value[fron-m]==' '|| value[fron-m]=='*'){
                        if(visited[fron-m]==0){
                            open.push(fron-m);
                            parent[fron-m]=fron;
                            visited[fron-m]=1;
                        }
                        
                    }
                    if(value[fron+1]==' '|| value[fron+1]=='*'){
                         if(visited[fron+1]==0){
                            open.push(fron+1);
                            parent[fron+1]=fron;
                            visited[fron+1]=1;
                        }
                       
                    }
                }
                else{
                    if(value[fron+m]==' '|| value[fron+m]=='*'){
                         if(visited[fron+m]==0){
                            open.push(fron+m);
                            parent[fron+m]=fron;
                            visited[fron+m]=1;
                        }
                    }
                    if(value[fron-m]==' '|| value[fron-m]=='*'){
                         if(visited[fron-m]==0){
                            open.push(fron-m);
                            parent[fron-m]=fron;
                            visited[fron-m]=1;
                        }
                       
                    }
                    if(value[fron+1]==' '|| value[fron+1]=='*'){
                         if(visited[fron+1]==0){
                            open.push(fron+1);
                            parent[fron+1]=fron;
                            visited[fron+1]=1;
                        }
                      
                    }
                }
            }
            else if((fron+1)%m==0){
                 if(value[fron+m]==' '|| value[fron+m]=='*'){
                         if(visited[fron+m]==0){
                            open.push(fron+m);
                            parent[fron+m]=fron;
                            visited[fron+m]=1;
                        }
                    }
                    if(value[fron-m]==' '|| value[fron-m]=='*'){
                         if(visited[fron-m]==0){
                            open.push(fron-m);
                            parent[fron-m]=fron;
                            visited[fron-m]=1;
                        }
                       
                    }
                    if(value[fron-1]==' '|| value[fron-1]=='*'){
                         if(visited[fron-1]==0){
                            open.push(fron-1);
                            parent[fron-1]=fron;
                            visited[fron-1]=1;
                        }
                      
                    }
            }
            else{  
                     if(value[fron+m]==' '|| value[fron+m]=='*'){
                         if(visited[fron+m]==0){
                            open.push(fron+m);
                            parent[fron+m]=fron;
                            visited[fron+m]=1;
                        }
                    }
                    if(value[fron-m]==' '|| value[fron-m]=='*'){
                         if(visited[fron-m]==0){
                            open.push(fron-m);
                            parent[fron-m]=fron;
                            visited[fron-m]=1;
                        }
                       
                    }
                    if(value[fron+1]==' '|| value[fron+1]=='*'){
                         if(visited[fron+1]==0){
                            open.push(fron+1);
                            parent[fron+1]=fron;
                            visited[fron+1]=1;
                        }
                      
                    }
                     if(value[fron-1]==' '|| value[fron-1]=='*'){
                         if(visited[fron-1]==0){
                            open.push(fron-1);
                            parent[fron-1]=fron;
                            visited[fron-1]=1;
                        }
                      
                    }
            }
            closed.push_back(fron);
            open.pop();
            state++;
        }
        int close=0;
        int paren=parent[fron];
        value[fron]='0';
        value[paren]='0';
        close++;
        while(paren!=-1){
            paren=parent[paren];
            value[paren]='0';
            close++;
        }
        cout<<state<<endl;
        cout<<close<<endl;
        for(int b=0;b<n;b++){
            for(int v=0;v<m;v++){
                cout<<value[m*b+v];
            }
            cout<<endl;
        }
    }
    else if(option==1){
        stack<int> open;
        open.push(0);
        while(!open.empty()){
            fron=open.top();
           // cout<<fron<<endl;
             open.pop();
            if(value[fron]=='*'){
                state++;
                break;
            }
            if(fron%m==0){
                if(fron==0){
                     if(value[fron+1]==' '|| value[fron+1]=='*'){
                         if(visited[fron+1]==0){
                            open.push(fron+1);
                            parent[fron+1]=fron;
                            visited[fron+1]=1;
                        }
                    }
                    if(value[fron+m]==' '|| value[fron+m]=='*'){
                         if(visited[fron+m]==0){
                            open.push(fron+m);
                            parent[fron+m]=fron;
                            visited[fron+m]=1;
                        }
                    }
                   
                }
                else if(fron==(m*(n-1))){
                     if(value[fron+1]==' '|| value[fron+1]=='*'){
                         if(visited[fron+1]==0){
                            open.push(fron+1);
                            parent[fron+1]=fron;
                            visited[fron+1]=1;
                        }
                       
                    }
                     if(value[fron-m]==' '|| value[fron-m]=='*'){
                        if(visited[fron-m]==0){
                            open.push(fron-m);
                            parent[fron-m]=fron;
                            visited[fron-m]=1;
                        }
                        
                    }
                   
                }
                else{
                      if(value[fron+1]==' '|| value[fron+1]=='*'){
                         if(visited[fron+1]==0){
                            open.push(fron+1);
                            parent[fron+1]=fron;
                            visited[fron+1]=1;
                        }
                      
                    }
                    if(value[fron-m]==' '|| value[fron-m]=='*'){
                         if(visited[fron-m]==0){
                            open.push(fron-m);
                            parent[fron-m]=fron;
                            visited[fron-m]=1;
                        }
                       
                    }
                     if(value[fron+m]==' '|| value[fron+m]=='*'){
                         if(visited[fron+m]==0){
                            open.push(fron+m);
                            parent[fron+m]=fron;
                            visited[fron+m]=1;
                        }
                    }
                  
                }
            }
            else if((fron+1)%m==0){
                 if(value[fron-1]==' '|| value[fron-1]=='*'){
                         if(visited[fron-1]==0){
                            open.push(fron-1);
                            parent[fron-1]=fron;
                            visited[fron-1]=1;
                        }
                      
                    }
                    if(value[fron-m]==' '|| value[fron-m]=='*'){
                         if(visited[fron-m]==0){
                            open.push(fron-m);
                            parent[fron-m]=fron;
                            visited[fron-m]=1;
                        }
                       
                    }
                     if(value[fron+m]==' '|| value[fron+m]=='*'){
                         if(visited[fron+m]==0){
                            open.push(fron+m);
                            parent[fron+m]=fron;
                            visited[fron+m]=1;
                        }
                    }
                   
            }
            else{  
                 if(value[fron-1]==' '|| value[fron-1]=='*'){
                         if(visited[fron-1]==0){
                            open.push(fron-1);
                            parent[fron-1]=fron;
                            visited[fron-1]=1;
                        }
                      
                    }
                  if(value[fron+1]==' '|| value[fron+1]=='*'){
                         if(visited[fron+1]==0){
                            open.push(fron+1);
                            parent[fron+1]=fron;
                            visited[fron+1]=1;
                        }
                      
                    }
                   if(value[fron-m]==' '|| value[fron-m]=='*'){
                         if(visited[fron-m]==0){
                            open.push(fron-m);
                            parent[fron-m]=fron;
                            visited[fron-m]=1;
                        }
                       
                    }
                     if(value[fron+m]==' '|| value[fron+m]=='*'){
                         if(visited[fron+m]==0){
                            open.push(fron+m);
                            parent[fron+m]=fron;
                            visited[fron+m]=1;
                        }
                    }
                   
                  
                  
            }
            closed.push_back(fron);
           
            state++;
        }

        int close=0;
        int paren=parent[fron];
        value[fron]='0';
        value[paren]='0';
        close++;
        while(paren!=-1){
            paren=parent[paren];
            value[paren]='0';
            close++;
        }
        cout<<state<<endl;
        cout<<close<<endl;
        for(int b=0;b<n;b++){
            for(int v=0;v<m;v++){
                cout<<value[m*b+v];
            }
            cout<<endl;
        }
    }

    if(option == 2) 
    {
        node[source].depth = 0;
        for(int i = 0;i < m1*n1;i++) 
        {
        	position* start = &node[source];
        	int depth = i;

        	if(start->depth < depth) 
		    {
		        start->visited = true;
		        if (start->data == dest) 
		        {
		            vari = alm;
		        }
		        alm++;
		        for(int i = 0;i < adj_list[start->data].arr.size();i++) 
		        {
		            if((adj_list[start->data].arr[i]->depth > start->depth + 1)) 
		            {
		                adj_list[start->data].arr[i]->parent = start;
		                adj_list[start->data].arr[i]->depth = start->depth + 1;

		                dfid(adj_list[start->data].arr[i],adj_list,depth,dest,node);
		            }
		        }
		    }

            for(int j = 0;j < m1*n1;j++) 
            {
                node[j].depth = 99999;
                node[i].visited = false;
                node[i].parent = NULL;
            }
            node[source].depth = 0;
            if(node[dest].visited == true) 
                break;
        }
    }

    if(option == 2)    
    {
        position* path = &node[dest];
        while(path->parent != NULL) 
        {
            int x = path->data / n1;
            int y = path->data % n1;
            maze[x][y] = '0';
            path = path->parent;
            length++;
        }
        maze[0][0] = '0';
        alm= vari - 1;
        cout << alm <<"\n"<< length <<"\n";
        for(int i = 0;i < maze.size(); i++) 
        {
            cout << maze[i] <<"\n";
        }
    }
}