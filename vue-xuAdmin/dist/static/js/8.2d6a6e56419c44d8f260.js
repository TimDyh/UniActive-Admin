(window.webpackJsonp=window.webpackJsonp||[]).push([[8],{"91Bc":function(t,e,n){},AnkQ:function(t,e,n){"use strict";n.r(e);var i=(n("hsAK"),n("QCOi")),a=Object(i.a)({name:"feedback",data:function(){return{input:"",feedbackList:[]}},mounted:function(){this.showFeedback()},methods:{showFeedback:function(){var t=this;this.$axios.get("http://114.115.134.188/api/get_feedback/").then((function(e){1===e.data.code&&(t.feedbackList=e.data.list)}))}}},(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticStyle:{padding:"10px"}},[n("div",{staticStyle:{background:"#fff","border-radius":"8px",padding:"8px"}},[n("div",[n("el-button",{attrs:{type:"primary"},on:{click:function(e){return t.showFeedback()}}},[t._v("刷新页面")])],1)]),t._v(" "),n("div",[n("el-table",{staticStyle:{width:"100%"},attrs:{data:t.feedbackList,border:""}},[n("el-table-column",{attrs:{type:"index","min-width":"10%"}}),t._v(" "),n("el-table-column",{attrs:{prop:"email",label:"账号","min-width":"20%"},scopedSlots:t._u([{key:"default",fn:function(e){return[t._v(" "+t._s(e.row.fields.provider)+" ")]}}])}),t._v(" "),n("el-table-column",{attrs:{prop:"opinion",label:"反馈时间","min-width":"20%"},scopedSlots:t._u([{key:"default",fn:function(e){return[t._v(" "+t._s(e.row.fields.time.replace(/T/g," ").replace(/Z/g,""))+" ")]}}])}),t._v(" "),n("el-table-column",{attrs:{prop:"opinion",label:"反馈意见","min-width":"50%"},scopedSlots:t._u([{key:"default",fn:function(e){return[t._v(" "+t._s(e.row.fields.opinion)+" ")]}}])})],1)],1)])}),[],!1,null,null,null);e.default=a.exports},hsAK:function(t,e,n){"use strict";var i=n("91Bc");n.n(i).a}}]);