from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render,redirect
from django.http import HttpResponse


class EmployeTable(APIView):



	def  get(self,request):
		emp = Employee.objects.all()
		serialzer = EmployeeSerializer(emp ,many=True)
		return Response(serialzer.data)


	def post(self,request):
		serialzerobj = EmployeeSerializer(data = request.data)
		if serialzerobj.is_valid():
			serialzerobj.save()
			return Response(serialzerobj.data,status=status.HTTP_201_CREATED)

		return Response(serialzerobj.data,status=status.HTTP_400_BAD_REQUEST)
			

class EmployeeUpdate(APIView):
	def get_objects(self,pk):
		try:
			return Employee.objects.get(pk=pk)
		except Employee.DoesNotExist:
			return Response(serialzerobj.data,status=status.HTTP_400_BAD_REQUEST)
			

	def get(self ,request,pk):
		emob = self.get_objects(pk)
		serialzerobj = EmployeeSerializer(emob)
		return Response(serialzerobj.data)


	def put(self,request,pk):
		emob = self.get_objects(pk)
		eserialize = EmployeeSerializer(emob,data=request.data)
		if eserialize.is_valid():
			return redirect('home')
		return Response(status = HTTP_400_BAD_REQUEST)


	def delete(self,request,pk):
		emob = self.get_objects(pk)
		emob.delete()
		return redirect('home')