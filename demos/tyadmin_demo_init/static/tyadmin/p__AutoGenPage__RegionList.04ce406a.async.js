(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[13,286],{"4KAj":function(e,t,n){"use strict";n.r(t);var r=n("q1tI"),a={icon:{tag:"svg",attrs:{viewBox:"64 64 896 896",focusable:"false"},children:[{tag:"path",attrs:{d:"M888.3 757.4h-53.8c-4.2 0-7.7 3.5-7.7 7.7v61.8H197.1V197.1h629.8v61.8c0 4.2 3.5 7.7 7.7 7.7h53.8c4.2 0 7.7-3.4 7.7-7.7V158.7c0-17-13.7-30.7-30.7-30.7H158.7c-17 0-30.7 13.7-30.7 30.7v706.6c0 17 13.7 30.7 30.7 30.7h706.6c17 0 30.7-13.7 30.7-30.7V765.1c0-4.3-3.5-7.7-7.7-7.7zm18.6-251.7L765 393.7c-5.3-4.2-13-.4-13 6.3v76H438c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h314v76c0 6.7 7.8 10.5 13 6.3l141.9-112a8 8 0 000-12.6z"}}]},name:"export",theme:"outlined"},c=a,u=n("6VBw"),i=function(e,t){return r["createElement"](u["a"],Object.assign({},e,{ref:t,icon:c}))};i.displayName="ExportOutlined";t["default"]=r["forwardRef"](i)},IpcI:function(e,t,n){e.exports={container:"container___nT1ry"}},PkmJ:function(e,t,n){"use strict";n("DZo9");var r=n("8z0m"),a=n("oBTY"),c=n("fWQN"),u=n("mtLc"),i=n("yKVA"),o=n("879j"),s=n("q1tI"),p=n.n(s),l=n("ye1Q"),f=n("xvlK"),d=n("IpcI"),b=n.n(d);function m(e,t){var n=new FileReader;n.addEventListener("load",(function(){return t(n.result)})),n.readAsDataURL(e)}var h=function(e){Object(i["a"])(n,e);var t=Object(o["a"])(n);function n(e){var r;return Object(c["a"])(this,n),r=t.call(this,e),r.state={loading:!1,fileList:[]},r.handleChange=function(e){var t=Object(a["a"])(e.fileList);t=t.slice(-1),t=t.map((function(e){return e.response&&(e.url=e.response.url),e})),r.props.onChange(e),e.file&&m(t[0].originFileObj,(function(e){return r.setState({fileList:t,imageUrl:e,loading:!1})}))},r}return Object(u["a"])(n,[{key:"render",value:function(e){var t=p.a.createElement("div",null,this.state.loading?p.a.createElement(l["default"],null):p.a.createElement(f["default"],null),p.a.createElement("div",{className:"ant-upload-text"},"Upload")),n=this.state.imageUrl;return"img"in this.props&&"string"==typeof this.props.img&&(n=this.props.img),p.a.createElement(r["a"],{name:"avatar",listType:"picture-card",showUploadList:!1,beforeUpload:this.props.beforeUpload,onChange:this.handleChange,fileList:this.state.fileList},n?p.a.createElement("img",{src:n,alt:"avatar",style:{width:"100%"}}):t)}}]),n}(p.a.Component);t["a"]=function(e){return p.a.createElement("div",{className:b.a.container},p.a.createElement("div",{id:"components-upload-demo-avatar"},p.a.createElement(h,e)))}},VHPH:function(e,t,n){"use strict";n.d(t,"b",(function(){return o})),n.d(t,"f",(function(){return p})),n.d(t,"a",(function(){return f})),n.d(t,"g",(function(){return b})),n.d(t,"e",(function(){return h})),n.d(t,"d",(function(){return j})),n.d(t,"c",(function(){return w}));n("k1fw");var r=n("WmNS"),a=n.n(r),c=n("9og8"),u=n("io9h"),i=n("+n12");function o(e){return s.apply(this,arguments)}function s(){return s=Object(c["a"])(a.a.mark((function e(t){return a.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.abrupt("return",Object(u["a"])("/api/xadmin/v1/city",{params:t}));case 1:case"end":return e.stop()}}),e)}))),s.apply(this,arguments)}function p(e){return l.apply(this,arguments)}function l(){return l=Object(c["a"])(a.a.mark((function e(t){return a.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.abrupt("return",Object(u["a"])("/api/xadmin/v1/city/".concat(t),{method:"DELETE"}));case 1:case"end":return e.stop()}}),e)}))),l.apply(this,arguments)}function f(e){return d.apply(this,arguments)}function d(){return d=Object(c["a"])(a.a.mark((function e(t){var n,r;return a.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return n=["image"],r=Object(i["c"])(t,n),e.abrupt("return",Object(u["a"])("/api/xadmin/v1/city",{method:"POST",data:r}));case 3:case"end":return e.stop()}}),e)}))),d.apply(this,arguments)}function b(e,t){return m.apply(this,arguments)}function m(){return m=Object(c["a"])(a.a.mark((function e(t,n){var r,c;return a.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return r=["image"],c=Object(i["c"])(t,r),e.abrupt("return",Object(u["a"])("/api/xadmin/v1/city/".concat(n),{method:"PUT",data:c}));case 3:case"end":return e.stop()}}),e)}))),m.apply(this,arguments)}function h(e){return O.apply(this,arguments)}function O(){return O=Object(c["a"])(a.a.mark((function e(t){return a.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.abrupt("return",Object(u["a"])("/api/xadmin/v1/city/verbose_name",{params:t}));case 1:case"end":return e.stop()}}),e)}))),O.apply(this,arguments)}function j(e){return v.apply(this,arguments)}function v(){return v=Object(c["a"])(a.a.mark((function e(t){return a.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.abrupt("return",Object(u["a"])("/api/xadmin/v1/city/list_display",{params:t}));case 1:case"end":return e.stop()}}),e)}))),v.apply(this,arguments)}function w(e){return y.apply(this,arguments)}function y(){return y=Object(c["a"])(a.a.mark((function e(t){return a.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.abrupt("return",Object(u["a"])("/api/xadmin/v1/city/display_order",{params:t}));case 1:case"end":return e.stop()}}),e)}))),y.apply(this,arguments)}},lzUk:function(e,t,n){"use strict";n.d(t,"b",(function(){return o})),n.d(t,"f",(function(){return p})),n.d(t,"a",(function(){return f})),n.d(t,"g",(function(){return b})),n.d(t,"e",(function(){return h})),n.d(t,"d",(function(){return j})),n.d(t,"c",(function(){return w}));n("k1fw");var r=n("WmNS"),a=n.n(r),c=n("9og8"),u=n("io9h"),i=n("+n12");function o(e){return s.apply(this,arguments)}function s(){return s=Object(c["a"])(a.a.mark((function e(t){return a.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.abrupt("return",Object(u["a"])("/api/xadmin/v1/region",{params:t}));case 1:case"end":return e.stop()}}),e)}))),s.apply(this,arguments)}function p(e){return l.apply(this,arguments)}function l(){return l=Object(c["a"])(a.a.mark((function e(t){return a.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.abrupt("return",Object(u["a"])("/api/xadmin/v1/region/".concat(t),{method:"DELETE"}));case 1:case"end":return e.stop()}}),e)}))),l.apply(this,arguments)}function f(e){return d.apply(this,arguments)}function d(){return d=Object(c["a"])(a.a.mark((function e(t){var n,r;return a.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return n=[],r=Object(i["c"])(t,n),e.abrupt("return",Object(u["a"])("/api/xadmin/v1/region",{method:"POST",data:r}));case 3:case"end":return e.stop()}}),e)}))),d.apply(this,arguments)}function b(e,t){return m.apply(this,arguments)}function m(){return m=Object(c["a"])(a.a.mark((function e(t,n){var r,c;return a.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return r=[],c=Object(i["c"])(t,r),e.abrupt("return",Object(u["a"])("/api/xadmin/v1/region/".concat(n),{method:"PUT",data:c}));case 3:case"end":return e.stop()}}),e)}))),m.apply(this,arguments)}function h(e){return O.apply(this,arguments)}function O(){return O=Object(c["a"])(a.a.mark((function e(t){return a.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.abrupt("return",Object(u["a"])("/api/xadmin/v1/region/verbose_name",{params:t}));case 1:case"end":return e.stop()}}),e)}))),O.apply(this,arguments)}function j(e){return v.apply(this,arguments)}function v(){return v=Object(c["a"])(a.a.mark((function e(t){return a.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.abrupt("return",Object(u["a"])("/api/xadmin/v1/region/list_display",{params:t}));case 1:case"end":return e.stop()}}),e)}))),v.apply(this,arguments)}function w(e){return y.apply(this,arguments)}function y(){return y=Object(c["a"])(a.a.mark((function e(t){return a.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.abrupt("return",Object(u["a"])("/api/xadmin/v1/region/display_order",{params:t}));case 1:case"end":return e.stop()}}),e)}))),y.apply(this,arguments)}},n2ZX:function(e,t,n){"use strict";n.r(t);n("qVdP");var r=n("jsC+"),a=(n("lUTK"),n("BvKs")),c=(n("5NDa"),n("5rEg")),u=(n("+L6B"),n("2/Rp")),i=n("oBTY"),o=(n("P2fV"),n("NJEC")),s=(n("/zsF"),n("PArb")),p=n("WmNS"),l=n.n(p),f=n("k1fw"),d=(n("miYZ"),n("tsqr")),b=n("9og8"),m=n("tJVT"),h=(n("y8nQ"),n("Vl3Y")),O=(n("OaEy"),n("2fM7")),j=n("G3dp"),v=n("/MfK"),w=n("xvlK"),y=n("4KAj"),x=n("8Skl"),g=n("q1tI"),k=n.n(g),E=n("Hx5s"),S=n("56R7"),_=(n("2qtc"),n("kLXV")),C=function(e){var t=e.modalVisible,n=e.onCancel;return k.a.createElement(_["a"],{destroyOnClose:!0,title:"\u65b0\u5efaregion",visible:t,width:800,onCancel:function(){return n()},footer:null},e.children)},I=C,T=n("lzUk"),R=function(e){var t=e.modalVisible,n=e.onCancel;return k.a.createElement(_["a"],{destroyOnClose:!0,title:"\u4fee\u6539region",visible:t,width:800,onCancel:function(){return n()},footer:null},e.children)},V=R,L=(n("PkmJ"),n("p2Up")),q=n("VHPH"),U=(n("wd/R"),n("+n12")),P=(n("Lzxq"),O["a"].Option,h["a"].Item,function(){var e=Object(g["useState"])(!1),t=Object(m["a"])(e,2),n=t[0],p=t[1],h=Object(g["useState"])(!1),O=Object(m["a"])(h,2),_=O[0],C=O[1],R=Object(g["useState"])({}),P=Object(m["a"])(R,2),K=P[0],N=P[1],A=Object(g["useRef"])(),z=Object(g["useRef"])(),H=Object(g["useRef"])(),B=function(){var e=Object(b["a"])(l.a.mark((function e(t){var n;return l.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return n=d["b"].loading("\u6b63\u5728\u6dfb\u52a0"),e.prev=1,e.next=4,Object(T["a"])(Object(f["a"])({},t));case 4:return n(),d["b"].success("\u6dfb\u52a0\u6210\u529f"),e.abrupt("return",!0);case 9:return e.prev=9,e.t0=e["catch"](1),e.abrupt("return",Object(U["e"])(e.t0,z,n,"\u6dfb\u52a0"));case 12:case"end":return e.stop()}}),e,null,[[1,9]])})));return function(t){return e.apply(this,arguments)}}(),F=function(){var e=Object(b["a"])(l.a.mark((function e(t,n){var r;return l.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return r=d["b"].loading("\u6b63\u5728\u4fee\u6539"),e.prev=1,e.next=4,Object(T["g"])(t,n);case 4:return r(),d["b"].success("\u4fee\u6539\u6210\u529f"),e.abrupt("return",!0);case 9:return e.prev=9,e.t0=e["catch"](1),e.abrupt("return",Object(U["e"])(e.t0,H,r,"\u4fee\u6539"));case 12:case"end":return e.stop()}}),e,null,[[1,9]])})));return function(t,n){return e.apply(this,arguments)}}(),D=function(){var e=Object(b["a"])(l.a.mark((function e(t){var n,r;return l.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:if(n=d["b"].loading("\u6b63\u5728\u5220\u9664"),t){e.next=3;break}return e.abrupt("return",!0);case 3:return e.prev=3,r=t.map((function(e){return e.id})).join(","),e.next=7,Object(T["f"])(r);case 7:return n(),d["b"].success("\u5220\u9664\u6210\u529f"),e.abrupt("return",!0);case 12:return e.prev=12,e.t0=e["catch"](3),n(),e.abrupt("return",Object(U["h"])(e.t0,"\u5220\u9664"));case 16:case"end":return e.stop()}}),e,null,[[3,12]])})));return function(t){return e.apply(this,arguments)}}(),J=[],W=[{title:"id",hideInForm:!0,hideInSearch:!0,dataIndex:"id",valueType:"digit",rules:[]},{title:"name",dataIndex:"name",rules:[{required:!0,message:"name\u4e3a\u5fc5\u586b\u9879"}]},{title:"population",dataIndex:"population",valueType:"digit",rules:[{required:!0,message:"population\u4e3a\u5fc5\u586b\u9879"}]},{title:"area",dataIndex:"area",rules:[{required:!0,message:"area\u4e3a\u5fc5\u586b\u9879"}]},{title:"zip_code",dataIndex:"zip_code",rules:[{required:!0,message:"zip_code\u4e3a\u5fc5\u586b\u9879"}]},{title:"super_admin",dataIndex:"super_admin",rules:[{required:!0,message:"super_admin\u4e3a\u5fc5\u586b\u9879"}],renderFormItem:function(e,t){var n=t.value,r=t.onChange;return Object(U["f"])(e,n,r,be)},render:function(e,t){return Object(U["u"])(e,je)}},{title:"city",dataIndex:"city",rules:[{required:!0,message:"city\u4e3a\u5fc5\u586b\u9879"}],renderFormItem:function(e,t){var n=t.value,r=t.onChange;return Object(U["f"])(e,n,r,xe)},render:function(e,t){return Object(U["u"])(e,Se)}},{title:"\u64cd\u4f5c",dataIndex:"option",valueType:"option",fixed:"right",width:100,render:function(e,t){return k.a.createElement(k.a.Fragment,null,k.a.createElement(j["default"],{title:"\u7f16\u8f91",className:"icon",onClick:Object(b["a"])(l.a.mark((function e(){return l.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:C(!0),N(t);case 2:case"end":return e.stop()}}),e)})))}),k.a.createElement(s["a"],{type:"vertical"}),k.a.createElement(o["a"],{title:"\u60a8\u786e\u5b9a\u8981\u5220\u9664region\u5417\uff1f",placement:"topRight",onConfirm:function(){D([t]),A.current.reloadAndRest()},okText:"\u786e\u5b9a",cancelText:"\u53d6\u6d88"},k.a.createElement(v["default"],{title:"\u5220\u9664",className:"icon"})))}}],M=Object(U["j"])(W),Y=Object(g["useState"])([]),Q=Object(m["a"])(Y,2),Z=Q[0],X=Q[1];Object(g["useEffect"])((function(){Object(T["c"])().then((function(e){X(e.form_order)}))}),[]);var G=Object(U["q"])(M),$=Object(U["j"])(W),ee=Object(U["s"])(Z,$),te=Object(i["a"])(ee),ne=Object(U["j"])(ee),re=Object(U["r"])(ne),ae=Object(g["useState"])({}),ce=Object(m["a"])(ae,2),ue=ce[0],ie=ce[1],oe=Object(g["useState"])({}),se=Object(m["a"])(oe,2),pe=se[0],le=se[1];Object(g["useEffect"])((function(){Object(T["d"])().then((function(e){ie(e)}))}),[]);var fe=Object(g["useState"])([]),de=Object(m["a"])(fe,2),be=de[0],me=de[1];Object(g["useEffect"])((function(){Object(L["b"])({all:1}).then((function(e){me(e)}))}),[]);var he=Object(g["useState"])([]),Oe=Object(m["a"])(he,2),je=Oe[0],ve=Oe[1];Object(g["useEffect"])((function(){Object(L["e"])().then((function(e){ve(e)}))}),[]);var we=Object(g["useState"])([]),ye=Object(m["a"])(we,2),xe=ye[0],ge=ye[1];Object(g["useEffect"])((function(){Object(q["b"])({all:1}).then((function(e){ge(e)}))}),[]);var ke=Object(g["useState"])([]),Ee=Object(m["a"])(ke,2),Se=Ee[0],_e=Ee[1];return Object(g["useEffect"])((function(){Object(q["e"])().then((function(e){_e(e)}))}),[]),k.a.createElement(E["c"],null,k.a.createElement(S["a"],{beforeSearchSubmit:function(e){return Object(U["i"])(e,J),e},params:pe,scroll:{x:"100%"},columnsStateMap:ue,onColumnsStateChange:function(e){return ie(e)},headerTitle:"region\u8868\u683c",actionRef:A,rowKey:"id",toolBarRender:function(e,t){var n=t.selectedRows;return[k.a.createElement(u["a"],{type:"primary",onClick:function(){return p(!0)}},k.a.createElement(w["default"],null)," \u65b0\u5efa"),k.a.createElement(u["a"],{type:"primary",onClick:function(){return Object(U["k"])(pe,T["b"],G,"region-All")}},k.a.createElement(y["default"],null)," \u5bfc\u51fa\u5168\u90e8"),k.a.createElement(c["a"].Search,{style:{marginRight:20},placeholder:"\u641c\u7d22region",onSearch:function(e){le({search:e}),A.current.reload()}}),n&&n.length>0&&k.a.createElement(r["a"],{overlay:k.a.createElement(a["a"],{onClick:function(){var e=Object(b["a"])(l.a.mark((function e(t){return l.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:if("remove"!==t.key){e.next=6;break}return e.next=3,D(n);case 3:A.current.reloadAndRest(),e.next=7;break;case 6:"export_current"===t.key&&Object(U["l"])(n,G,"region-select");case 7:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),selectedKeys:[]},k.a.createElement(a["a"].Item,{key:"remove"},"\u6279\u91cf\u5220\u9664"),k.a.createElement(a["a"].Item,{key:"export_current"},"\u5bfc\u51fa\u5df2\u9009"))},k.a.createElement(u["a"],null,"\u6279\u91cf\u64cd\u4f5c ",k.a.createElement(x["default"],null)))]},tableAlertRender:function(e){var t=e.selectedRowKeys;e.selectedRows;return t.length>0&&k.a.createElement("div",null,"\u5df2\u9009\u62e9"," ",k.a.createElement("a",{style:{fontWeight:600}},t.length)," ","\u9879\xa0\xa0")},request:function(e,t,n){return Object(T["b"])(Object(f["a"])(Object(f["a"])({},e),{},{sorter:t,filter:n}))},columns:G,rowSelection:{}}),k.a.createElement(I,{onCancel:function(){return p(!1)},modalVisible:n},k.a.createElement(S["a"],{formRef:z,onSubmit:function(){var e=Object(b["a"])(l.a.mark((function e(t){var n;return l.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return Object(U["w"])(t),e.next=3,B(t);case 3:n=e.sent,n&&(p(!1),A.current&&A.current.reload());case 5:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),rowKey:"key",type:"form",search:{},form:{labelCol:{span:6},labelAlign:"left"},columns:te,rowSelection:{}})),k.a.createElement(V,{onCancel:function(){return C(!1)},modalVisible:_},k.a.createElement(S["a"],{formRef:H,onSubmit:function(){var e=Object(b["a"])(l.a.mark((function e(t){var n;return l.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return Object(U["w"])(t),e.next=3,F(t,K.id);case 3:n=e.sent,n&&(C(!1),A.current&&A.current.reload());case 5:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),rowKey:"key",search:{},type:"form",form:{initialValues:K,labelCol:{span:6},labelAlign:"left"},columns:re,rowSelection:{}})))});t["default"]=P},p2Up:function(e,t,n){"use strict";n.d(t,"b",(function(){return s})),n.d(t,"f",(function(){return l})),n.d(t,"a",(function(){return d})),n.d(t,"h",(function(){return m})),n.d(t,"e",(function(){return O})),n.d(t,"d",(function(){return v})),n.d(t,"c",(function(){return y})),n.d(t,"g",(function(){return g}));var r=n("k1fw"),a=n("WmNS"),c=n.n(a),u=n("9og8"),i=n("io9h"),o=n("+n12");function s(e){return p.apply(this,arguments)}function p(){return p=Object(u["a"])(c.a.mark((function e(t){return c.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.abrupt("return",Object(i["a"])("/api/xadmin/v1/user_profile",{params:t}));case 1:case"end":return e.stop()}}),e)}))),p.apply(this,arguments)}function l(e){return f.apply(this,arguments)}function f(){return f=Object(u["a"])(c.a.mark((function e(t){return c.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.abrupt("return",Object(i["a"])("/api/xadmin/v1/user_profile/".concat(t),{method:"DELETE"}));case 1:case"end":return e.stop()}}),e)}))),f.apply(this,arguments)}function d(e){return b.apply(this,arguments)}function b(){return b=Object(u["a"])(c.a.mark((function e(t){var n,r;return c.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return n=["image"],r=Object(o["c"])(t,n),e.abrupt("return",Object(i["a"])("/api/xadmin/v1/user_profile",{method:"POST",data:r}));case 3:case"end":return e.stop()}}),e)}))),b.apply(this,arguments)}function m(e,t){return h.apply(this,arguments)}function h(){return h=Object(u["a"])(c.a.mark((function e(t,n){var r,a;return c.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return r=["image"],a=Object(o["c"])(t,r),e.abrupt("return",Object(i["a"])("/api/xadmin/v1/user_profile/".concat(n),{method:"PUT",data:a}));case 3:case"end":return e.stop()}}),e)}))),h.apply(this,arguments)}function O(e){return j.apply(this,arguments)}function j(){return j=Object(u["a"])(c.a.mark((function e(t){return c.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.abrupt("return",Object(i["a"])("/api/xadmin/v1/user_profile/verbose_name",{params:t}));case 1:case"end":return e.stop()}}),e)}))),j.apply(this,arguments)}function v(e){return w.apply(this,arguments)}function w(){return w=Object(u["a"])(c.a.mark((function e(t){return c.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.abrupt("return",Object(i["a"])("/api/xadmin/v1/user_profile/list_display",{params:t}));case 1:case"end":return e.stop()}}),e)}))),w.apply(this,arguments)}function y(e){return x.apply(this,arguments)}function x(){return x=Object(u["a"])(c.a.mark((function e(t){return c.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.abrupt("return",Object(i["a"])("/api/xadmin/v1/user_profile/display_order",{params:t}));case 1:case"end":return e.stop()}}),e)}))),x.apply(this,arguments)}function g(e){return k.apply(this,arguments)}function k(){return k=Object(u["a"])(c.a.mark((function e(t){return c.a.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.abrupt("return",Object(i["a"])("/api/xadmin/v1/list_change_password",{method:"POST",data:Object(r["a"])({},t)}));case 1:case"end":return e.stop()}}),e)}))),k.apply(this,arguments)}}}]);