#coding: utf-8
#importando os modulos para criar o serviço
import win32service
import win32serviceutil
import win32event

class Isca((win32serviceutil.ServiceFramework)):
	_svc_name_ = "I.S.C.A-PY"
	_svc_display_name_ = "I.S.C.A" 
	_svc_description_ = "This is robot's service BITFARMA" 

	def __inti__(self, args):

		win32serviceutil.ServiceFramework.__init__(self, args)
		self.hWaitStop = win32event.CreateEvent(None, 0 , 0 , None)

	def inciar_servicos(self):
		import servicemanager
		arq = open('test.dat', 'w+')
		rc = None
		while rc != win32event.Wait_OBJECT_0:
		 	arq.write('Gravando...')
		 	f.flush()

		 	rc = win32event.WaitForsingleObject(self.hWaitStop, 5000)
		arq.write('fechando...')
		arq.close()

		def para_servicos(self):
		 	self.ReportServicesStatus(win32service.SERVICE_STOP_PENDING)
		 	win32event.SetEvent(self.hWaitStop)
if __name__ == '__main__':  
    win32serviceutil.HandleCommandLine(Isca)   

