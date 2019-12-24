new Vue({
  delimiters:['[[',']]'],
  el:'#index',
  data:{
    topmenu:[],
    banner:[],
    userUI:false,
    loginType:false,
    username:'',
    password:''
  },
  mounted(){
    this.getData()
    console.log(this)
  },
  methods:{
    getData:function(){
      var self = this
      reqwest({
        url:'/api/index',
        method: 'get',
        type:'json',
        success:function(data){
          console.log(data)
          self.topmenu = data.topmenu
          self.banner = data.banner
          if(data.loginType == 'ok'){
            self.loginType = true
          }else{
            self.loginType = false
          }
          // console.log(self.topmenu)
        }
      })
    },
    userLogin:function(){
      var self = this
      reqwest({
        url:'/api/index',
        method:'post',
        type:'json',
        headers:{
          "X-CSRFTOKEN":csrftoken
        },
        data:{
          username:self.username,
          password:self.password
        },
        success:function(data){
          console.log('ok')
          console.log(data)
          if (data.loginType=='ok') {
            self.userUI = false
            self.loginType = true
          }
        },
        error:function(err){
          console.log(err)
        }
      })
    },
    showUserUI:function(){
      this.userUI = !this.userUI
    },
    toadmin:function() {
      window.location.href = '/Dwebadmin'
    }
  }
})
