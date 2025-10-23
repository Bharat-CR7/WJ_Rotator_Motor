#ifndef _WJ_API_
#define _WJ_API_

//#include <assert.h>
//#include <windows.h>


#pragma comment(lib,"WJ_API.lib")

#ifdef __cplusplus
#define WJ_API extern "C" __declspec( dllexport )
#else
#define WJ_API __declspec( dllexport )
#endif


//ͨ�ų�ʼ��ָ��
WJ_API INT32 __stdcall WJ_Open(int num_scom);//���ںţ�0ΪUSB����
WJ_API INT32 __stdcall WJ_Close();


//��ѯָ��

WJ_API INT32 __stdcall WJ_Get_Axis_Acc(INT32 AxisNUM, INT32* pValue);

WJ_API INT32 __stdcall WJ_Get_Axis_Dec(INT32 AxisNUM, INT32* pValue);

WJ_API INT32 __stdcall WJ_Get_Axis_Vel(INT32 AxisNUM, INT32* pValue);

WJ_API INT32 __stdcall WJ_Get_Axis_Subdivision(INT32 AxisNUM, INT32* pValue);

WJ_API INT32 __stdcall WJ_Get_Axis_Status(INT32 AxisNUM, INT32* pValue);

WJ_API INT32 __stdcall WJ_Get_Axes_Status(INT32 pValueAxes[]);

WJ_API INT32 __stdcall WJ_Get_Axis_Pulses(INT32 AxisNUM, INT32* pValue);

WJ_API INT32 __stdcall WJ_Get_Axes_Pulses(INT32 pValueAxes[]);

WJ_API INT32 __stdcall WJ_Get_Axes_Num(INT32* pValue);//��ѯ���������ݰ忨��ͬ����4��8����Ӧָ��Q07


//�˶�ָ��
WJ_API INT32 __stdcall WJ_Move_Axis_Pulses(INT32 AxisNUM, INT32 Value);

WJ_API INT32 __stdcall WJ_Move_Axes_Pulses(INT32 pValueAxes[]);///

WJ_API INT32 __stdcall WJ_Move_Axis_Vel(INT32 AxisNUM, INT32 Value);

WJ_API INT32 __stdcall WJ_Move_Axes_Vel(INT32 pValueAxes[]);

WJ_API INT32 __stdcall WJ_Move_Axis_Emergency_Stop(INT32 AxisNUM);

WJ_API INT32 __stdcall WJ_Move_Axis_Slow_Stop(INT32 AxisNUM);

WJ_API INT32 __stdcall WJ_Move_Axis_Home(INT32 AxisNUM, INT32 Value);



//����ָ��

WJ_API INT32 __stdcall WJ_Set_Axis_Acc(INT32 AxisNUM, INT32 Value);

WJ_API INT32 __stdcall WJ_Set_Axis_Dec(INT32 AxisNUM, INT32 Value);

WJ_API INT32 __stdcall WJ_Set_Axis_Vel(INT32 AxisNUM, INT32 Value);

WJ_API INT32 __stdcall WJ_Set_Axis_Subdivision(INT32 AxisNUM, INT32 Value);

WJ_API INT32 __stdcall WJ_Set_Axis_Slow_Stop(INT32 AxisNUM, INT32 Value);

WJ_API INT32 __stdcall WJ_Set_Led_Twinkle();

WJ_API INT32 __stdcall WJ_Set_Axis_Pulses_Zero(INT32 AxisNUM);

WJ_API INT32 __stdcall WJ_Set_Default();

WJ_API INT32 __stdcall WJ_Set_Move_Axis_Vel_Acc(INT32 AxisNUM, INT32 Value);

WJ_API INT32 __stdcall WJ_Set_Axis_Home_Pulses(INT32 AxisNUM, INT32 Value);

//IOָ��
WJ_API INT32 __stdcall WJ_IO_Output(INT32 IONUM, INT32 Value);

WJ_API INT32 __stdcall WJ_IO_Input(INT32 IONUM, INT32* pValue);


#endif
