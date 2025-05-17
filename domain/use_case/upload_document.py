from domain.interfaces.upload_document_interface import Document

class UploadDocumentUseCase:
    def __init__(self, document: Document):
        self.document = document

    def apply(self, object_name, bucket_name, body):
        print("applying UploadDocumentUseCase")
        response =  self.document.upload_document(object_name, bucket_name, body)
        if not response:
            return {
                "message": "Error, no se retorno la respuesta"
            }
        return  response
            
