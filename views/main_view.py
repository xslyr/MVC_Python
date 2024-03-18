
from flask import render_template
from controllers.app_types import TControllerResponse

class ViewFactory:
	
	@classmethod
	def send_view(self, controller_request:TControllerResponse ):
		
		match controller_request.view:
			case 'main': template = 'main.html'
			case _: return 'View não configurada.'
		
		return render_template( template, info=controller_request.args)
