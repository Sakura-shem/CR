<template>
    <div class="main">
        <nav>
            <img src="@/assets/logo.png"/>
            <h1>233</h1>
        </nav>
        <el-scrollbar>
            <div class="content">
                <Msg v-for="(item,i) in msg" :key="i" :direction="item.direction" :name="item.name"/>
            </div>   
        </el-scrollbar>
        <div class="sendBox">
            <!-- <div class="send">
                <el-button type="primary">发送</el-button>
            </div> -->
            <el-input
                v-model="sendMessage"
                :autosize="{ minRows: 4, maxRows: 6 }"
                type="textarea"
                placeholder="输入消息"
                style="width: 100%;"
                resize="none"
            />
        </div>
        <div class="more">
            <el-icon><Microphone /></el-icon>
            <el-icon><Picture /></el-icon>
            <el-icon><Camera /></el-icon>
            <el-icon><ChromeFilled /></el-icon>
            <el-icon><CirclePlus /></el-icon>
        </div>
    </div>
</template>

<script>
// import {ElCarousel,ElCarouselItem} from "element-plus";
import Msg from "@/components/cr-message.vue";
import {
    CirclePlus,Picture,Camera,ChromeFilled,Microphone
} from '@element-plus/icons-vue'


export default{
    components:{
        Msg,
        Microphone,CirclePlus,Picture,Camera,ChromeFilled
    },
    data(){
        return {
            sendMessage:"",
            msg:[
                {name:"sdsdsds",direction:true},
                {name:"asdfg2",direction:false},
                {name:"asdasdsd",direction:true},
                {name:"asdfg2",direction:false},
                {name:"asdfg2",direction:false},
                {name:"asdasdasd",direction:true},
                {name:"asdfg",direction:true},
                {name:"asdasd",direction:true},
                {name:"asdfg2",direction:false},
                {name:"asdfg2",direction:false},
                {name:"asdfg2",direction:false},
                {name:"asdfg2",direction:false},
                {name:"asdasdasd",direction:true},
                {name:"asdfg2",direction:false},
                {name:"asdfg",direction:true},
            ]
        }
    }
}


</script>


<style scoped>

.main{
    width: 100%;
    height: 100%;
    background-color: #F5F7F9;
    display: flex;
    flex-direction: column;
    justify-content: center;    
}
nav{
    background-color: #909399;
    height: 63.5px;
    overflow: hidden;
    display: flex;
    align-items: center;
}
nav>img{
    width: 45px;
    height: 45px;
    margin-left: 30px;
}
nav>h1{
    color: white;
    margin-left: 10px;
}

.content{
    flex: 1;
    padding: 20px;
}

.sendBox{
    display: flex;
    padding: 5px;
}

.more{
    display: flex;
    justify-content: space-between;
    padding-left: 20px;
    padding-right: 20px;
    margin-top: 10px;
    margin-bottom: 10px;
}

.el-icon{
    font-size: 30px;
}

</style>

<style>
.el-textarea__inner::-webkit-scrollbar {
    width: 7px;
    height: 7px;
}
.el-textarea__inner::-webkit-scrollbar-track {
    background-color: #ffffff;
}
.el-textarea__inner::-webkit-scrollbar-thumb {
    background-color: rgba(144, 147, 153, 0.3);
    border-radius: 5px;
    border: 1px solid #f1f1f1;
    box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.1);
}
.el-textarea__inner::-webkit-scrollbar-thumb:hover {
    background-color: rgba(144, 147, 153, 0.3);
}
.el-textarea__inner::-webkit-scrollbar-thumb:active {
    background-color: rgba(144, 147, 153, 0.3);
}
.el-textarea__inner::-webkit-scrollbar-corner {
    background-color: #ffffff;
}
</style>