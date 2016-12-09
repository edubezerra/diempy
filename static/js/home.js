/****************************************************************************************************************************************/
/*** Diemp										*/
/*** Autor					: Iury Amorim		*/
/*** Data de Criação		: 04/07/2016		*/
/*** Data de Modificação	: 04/07/2016		*/
/************************************************/

/****************************************************************************************************************************************/ 
var oHome = {
	jqThis : null
	
	, Carregar: function () {
		var _this = this;

		_this.jqThis = jQuery('#jqHome');

		var sHash = window.location.hash;

		if (sHash.length) { _this.MoverParaAncora(sHash); }                                       

		if (_this.jqThis.length){             
			_this.CarregarEventos();
		}
	}
	, CarregarEventos: function () {
		var _this = this;
		jQuery('a[rel="jqAncoraHome"]').bind('click', function () { _this.MoverParaAncora(jQuery(this).attr('href')); });
		
	}
	, MoverParaAncora: function (psHash) {
		var _this = this;
	
		var oJqElemento = jQuery('.jqAncoraHome[rel="' + psHash + '"]');
	
		if (oJqElemento.length) {
			jQuery('body').animate({ scrollTop: (oJqElemento.offset().top)-50 }, 500);
		}
	}
};
/****************************************************************************************************************************************/ 
jQuery(window).load(function () {
	oHome.Carregar();
});
/****************************************************************************************************************************************/