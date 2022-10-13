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
        <div style="position: relative;">
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
    </div>
</template>

<script>
// import {ElCarousel,ElCarouselItem} from "element-plus";
import Msg from "@/components/cr-message.vue";

export default{
    components:{
        Msg
    },
    data(){
        return {
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

</style>
