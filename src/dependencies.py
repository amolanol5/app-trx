from src.controllers.out.upload_document_adapter import DocumentAdapter
from domain.use_case.upload_document import UploadDocumentUseCase

document_adapter = DocumentAdapter()
service_document = UploadDocumentUseCase(document_adapter)

