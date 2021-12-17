import request from "@/api/utils"

export function projectAdd(name,describe){
    return request({
        url:"project",
        method:"POST",
        data:{
            name,describe
        }
    })
}

export function projectGet(){
    return request({
        url:"project",
        method:"GET",

    })
}

export function modelAdd(name,describe,projectId){
    return request({
        url:"modelss",
        method:"POST",
        data:{
            name,describe,projectId
        }
    })
}

export function modelGet(id){
    return request({
        url:"modelss",
        method:"GET",
        params:{
            "id":id,
        }

    })
}