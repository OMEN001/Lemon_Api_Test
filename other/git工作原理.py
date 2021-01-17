#_*_conding:utf-8_*_
#@Time    :2020/3/818:20
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com

"""
git的基本概念
remote  远程仓库
repository 本地仓库
workspace 工作区  存放项目目录文件的区域，开发工作内容就是在工作区域进行（如：pycharm）
index 暂存区  介于工作区间和本地仓库（版本库）之间，要提交到版本库的问价必须先暂存到这个区域

最常用的git命令
git add 文件名   --将工作区的指定文件添加的暂存区
git commit -m "注释"  --将暂存区的文件提交到本地仓库并产生一个新的版本
git push --将本地仓库的最新内容推送到远程

.git如何进行代码管理（结合pycharm）   3.6注册github账号并使用GITUI 和gitbash(结合pycharm)
（1）如何进行代码的提交与下载    OK
（2）如何使用git创建分支         OK

Git Bash Here操作命令
（1）github 创建项目的操作步骤
	第一步：点击GitHub首页（左侧的🐱图标）
	第二步：创建一个项目（start a project）
	第三步：填写仓库的名称、仓库描述、选择公共或者私有仓库（public、private）然后点击 Create repository
 (2)Git Bash Here 配置sshkey(主要作用是用于客户端与GitHub的身份验证)
	第一步：在Git Bash Here命令行中输入如下的命令
  	             ssh-keygen -t rsa -C "注册的GitHub账号邮件地址" （会提示在本地的目录生成一个 .ssh文件主要包含用于验证身份的公钥与私钥）
	第二步：id_rsa(私钥)、id_rsa.pub(公钥) 打开公钥文件并复制文件内容
	第三步：在GitHub首页点击页面顶部最右侧的设置图标，下拉列表中点击Settings
	第四步：在设置页面点击SSH and GPG keys
	第五步：SSH  keys栏中点击 New SSH key,在SSH key页面填写titlle并将公钥复制到key输入栏中，然后点击 Add SSH key
 (2)将GitHub中的仓库克隆到本地（前提是在本地提前创建一个工作目录用于克隆仓库）
	第一步：将目录切换到创建的工作目录盘符中
	第二步：执行git clone "GitHub中仓库的https"
	第三步：本地会生成一个仓库
（3）Git Bash Here 中如何将代码推送到远程仓库及分支的创建、删除、合并
	(1)代码的提交（一定要将目录切换到克隆仓库的路径下）
	     查看未被追踪的文件: git status
	     追踪文件：dit add  文件名 ，如果是多个文件用 git add . (这里有一点)
	     提交文件：git commit -m "提交注释或者是说明"
	     推送到远程仓库： git push    或者 git push origin <本地分支>:<远程分支>  例如： git push origin  master:master(git push origin  master)从本地的主分支推送到远程的主分支
   	(2)创建、切换、合并（合并之后push主分支的文件到远程就可以）、删除、并推送到远程(注意步骤(1)、(2)、(3)、(4)仅限于在本地，如要同步需git push到远程)
	     (1)创建分支(一般在主分支master中操作)：git branch 分支名称  例如：git branch dev
                     创建并切换到分支： git checkout -b 分支名称
	     (2)切换分支：git checkout 分支名称、git switch 分支名称
	     (3)删除分支：git branch -d 	分支名称
	     (4)合并分支(要将目录切换到主分支在进行合并)：git merge 分支名称
	    删除分支本地分支及远程(Git Bash中删除分支要在主分支下进行操作)：git push origin 【空格】【冒号】【需要删除的分支名字】 例如：git push origin :branch1
	    通过GitHub删除分支：
 		#仓库主页（能看到仓库内容的页面),点击branch进入到分支页面
		#点击要删除分支后面的删除按钮即可删除
	    创建分支并提交到远程(GitHub这里需注意要切换到新创建的分支下执行此命令):  git push origin HEAD -
"""


