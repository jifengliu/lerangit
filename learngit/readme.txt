Git is a distributed version control system.
Git is free software distributed under the GPL.
Git has a mutable index called stage.

//ssh生成的.pub文件查看
//使用cd命令进入id_rsa.pub目录: 
cd ~/.ssh
//再使用命令查看公钥的内容,三个命令均可:  
more id_rsa.pub 
open .ssh/id_rsa.pub 
cat .ssh/id_rsa.pub 

//公钥验证连接
ssh -T git@github.com

//设置username和email（github每次commit都会记录他们）
git config --global user.name "jifengliu"
git config --global user.email "jifengliu@139.com"

//文件添加到仓库（.代表提交所有文件）
git add .
//把文件提交到仓库
git commit -m "First Commit"
//上传到github
git push

