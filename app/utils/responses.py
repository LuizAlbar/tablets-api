from fastapi import HTTPException, status

class ResponseHandler:
    
    @staticmethod
    def sucess(message, data = None):
        return {"message" : message, "data": data}
    
    @staticmethod
    def get_single_success(name, id, data):
        message = f"Details for {name} with id {id}"
        return ResponseHandler.sucess(message, data)
    
    @staticmethod
    def create_success(name, id, data):
        message = f"{name} with id {id} created successfully"
        return ResponseHandler.sucess(message, data)
    
    @staticmethod
    def update_sucess(name, id, data):
        message = f"{name} with id {id} updated sucessfully"
        return ResponseHandler.sucess(message, data)
    
    @staticmethod
    def delete_success(name, id, data):
        message = f"{name} with id {id} deleted sucessfully"
        return ResponseHandler.sucess(message, data)
    
    @staticmethod
    def not_found_error(name = "", id = None):
        message = f"{name} with id {id} not found!"
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= message)