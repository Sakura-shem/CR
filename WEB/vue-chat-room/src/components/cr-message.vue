<template>
    <div :class="layout">
        <el-icon><User /></el-icon>
        <div class="content">
            <span class="ban-select-font">{{name}}</span>
            <article>
                Lorem ipsum dolor, sit amet consectetur adipisicing elit. Placeat rerum eveniet officiis facilis atque voluptatem inventore ullam debitis aliquam expedita dolorem architecto quaerat voluptatum fugiat voluptas, impedit, eius quae ratione?
            </article>
        </div>
    </div>
</template>

<script>

import { ElIcon } from 'element-plus';
import { User } from '@element-plus/icons-vue';

export default{
    name:'cr-message',
    components:{
        ElIcon,User
    },
    props:{
        direction:{
            type:Boolean,
            default:true
        },
        name:{
            type:String,
            default:"user233"
        }
    },
    computed:{
        layout(){
            return (this.direction)?"msg":"msg2";
        }
    },
}

</script>

<style scoped>
.msg{
    width: 100%;
    display: flex;
    align-items: flex-start;
    margin-bottom: 15px;
}

.msg2{
    width: 100%;
    display: flex;
    flex-direction: row-reverse;
    align-items: flex-start;
    margin-bottom: 15px;
}

.el-icon{
    width: 20px;
    height: 20px;
    font-size: 20px;
    border: 1px solid black;
    border-radius: 6px;
}

.msg2 .el-icon{
    color: #00A4FF;
}

.msg .content{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.msg2 .content{
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}

.msg span{
    margin-left: 10px;
}

.msg2 span{
    margin-right: 10px;
}

.msg article{
    margin-left: 5px;
    border: 1px solid grey;
    border-radius: .5rem;
    background-color: #FFFFFF;
}
.msg article:hover{
    text-shadow: .3px .3px gray;
    box-shadow: .3px .3px gray;
}

.msg2 article{
    margin-left: 5px;
    border: 1px solid grey;
    border-radius: .5rem;
    background-color: #00A4FF;
}
.msg2 article:hover{
    text-shadow: .3px .3px gray;
    box-shadow: .3px .3px gray;
}


</style>