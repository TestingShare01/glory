import request from "@/api/utils"

// 添加项目
export function projectAdd(name,describe){
    return request({
        url:"project",
        method:"POST",
        data:{
            name,describe
        }
    })
}

// 获取项目列表数据
export function projectGet(){
    return request({
        url:"project",
        method:"GET",

    })
}

// 添加模块
export function modelAdd(name,describe,projectId){
    return request({
        url:"modelss",
        method:"POST",
        data:{
            name,describe,projectId
        }
    })
}

//获取所有模块
export function getModel(){
    return request({
        url:"modelss",
        method:"GET"
    })
}

// 获取模块列表数据
export function modelGet(id){
    return request({
        url:"modelss",
        method:"GET",
        params:{
            "id":id,
        }

    })
}

// 单接口运行
export function oneCase(id,method,url,datas,headers,result,cookies){
    return request({
        url:"jkCase",
        method:"POST",
        data:{
            id,method,url,datas,headers,result,cookies
        }
    })
}


//添加接口保存
export function apiSave(id,user,name,remark,priority,mokuai,tag,url,selectmethod,datas,headers,cookies,resultPk){
    return request({
        url:"jkSave",
        method:"POST",
        data:{
            id,user,name,remark,priority,mokuai,tag,url,selectmethod,datas,headers,cookies,resultPk
        }
    })
}

//获取接口list
export function getApiList(){
    return request({
        url:"jkSave",
        method:"GET",
    })
}

// 获取单接口数据
export function getOneCase(id){
    return request({
        url:"jkSave",
        method:"GET",
        params:{
            id
        }
    })
}

//获取标签list
export function getTagList(){
    return request({
        url:"tag",
        method:"GET"
    })
}

// 创建任务
export function makeTasks(id_list,name,username){
    return request({
        url:"task",
        method:"POST",
        data:{
            id_list,name,username,
        }
    })
}

// 获取任务
export function getTask(id){
    return request({
        url:"task",
        method:"GET",
        params:{
            id
        }
    })
}

//删除接口数据
export function delCaseApi(id){
    return request({
        url:"jkCase",
        method:"GET",
        params:{
            id
        }
    })
}

// 执行任务
export function zxTask(id,user){
    return request({
        url:"zxTaskCase",
        method:"POST",
        data:{
            id,user
        }
    })
}

// 获取报告数据
export function getReport(id,page){
    return request({
        url:"reportInfo",
        method:"GET",
        params:{
            id,page
        }
    })
}

// 定时任务
export function Cron(id,cron){
    return request({
        url:"timetask",
        method:"POST",
        data:{
            id,cron
        }
    })
}

// 删除任务
export function delTask(id){
    return request({
        url:"zxTaskCase",
        method:"GET",
        params:{
            id
        }
    })
}

//报告详情
export function reportdetai(id){
    return request({
        url:"reportDetail",
        method:"GET",
        params:{
            id
        }
    })
}

// 删除定时
export function delTimin(id){
    return request({
        url:"timetask",
        method:"GET",
        params:{
            id
        }
    })
}

//获取日志数据
export function getlog(id){
    return request({
        url:"caseLogInfo",
        method:"GET",
        params:{
            id
        }
    })
}

//登录
export function login(user,pwd){
    return request({
        url:"Login",
        method:"POST",
        data:{
            user,pwd
        }
    })
}

// 总数量
export function getNums(){
    return request({
        url:"getNum",
        method:"GET",

    })
}

// 创建全局
export function createGload(taskId,parameter,values){
    return request({
        url:"gloabs",
        method:"POST",
        data:{
            taskId,parameter,values
        }
    })
}

//获取单个任务全局内容
export function getGload(taskId){
    return request({
        url:"gloabs",
        method:"GET",
        params:{
            taskId
        }
    })
}

//保存接口中的提取器内容
export function SaveTiquValue(caseId,tiquList){
    return request({
        url:"variable",
        method:"POST",
        data:{
            caseId,tiquList
        }
    })
}

//获取提取器中的所有内容
export function getTiqu(){
    return request({
        url:"variable",
        method:"GET"
    })
}

// 添加环境配置
export function envSet(envName){
    return request({
        url:"envSetting",
        method:"POST",
        data:{
            envName
        }
    })
}

// 获取环境配置数据
export function getEnv(){
    return request({
        url:"envSetting",
        method:"GET",
    })
}


// 添加环境ip域名配置
export function envIp(envId,domain,ip){
    return request({
        url:"envSetting",
        method:"POST",
        data:{
            envId,domain,ip
        }
    })
}

// 获取环境ip域名配置数据
export function getIp(envId){
    return request({
        url:"envSetting",
        method:"GET",
        params:{
            envId
        }
    })
}

//URL导入域名
export function addurl(envId,url){
    return request({
        url:"urlAdd",
        method:"POST",
        data:{
            envId,url
        }
    })
}

//接口列表页筛选功能
export function selectApi(tag,mokuai,priority,select){
    return request({
        url:"jkSave",
        method:"GET",
        params:{
            tag,mokuai,priority,select
        }
    })
}