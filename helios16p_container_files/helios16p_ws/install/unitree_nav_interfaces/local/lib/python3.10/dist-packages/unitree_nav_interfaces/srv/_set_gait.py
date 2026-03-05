# generated from rosidl_generator_py/resource/_idl.py.em
# with input from unitree_nav_interfaces:srv/SetGait.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SetGait_Request(type):
    """Metaclass of message 'SetGait_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'IDLE': 0,
        'TROT': 1,
        'TROT_RUNNING': 2,
        'CLIMB_STAIRS': 3,
        'TROT_OBSTACLE': 4,
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('unitree_nav_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'unitree_nav_interfaces.srv.SetGait_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_gait__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_gait__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_gait__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_gait__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_gait__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'IDLE': cls.__constants['IDLE'],
            'TROT': cls.__constants['TROT'],
            'TROT_RUNNING': cls.__constants['TROT_RUNNING'],
            'CLIMB_STAIRS': cls.__constants['CLIMB_STAIRS'],
            'TROT_OBSTACLE': cls.__constants['TROT_OBSTACLE'],
        }

    @property
    def IDLE(self):
        """Message constant 'IDLE'."""
        return Metaclass_SetGait_Request.__constants['IDLE']

    @property
    def TROT(self):
        """Message constant 'TROT'."""
        return Metaclass_SetGait_Request.__constants['TROT']

    @property
    def TROT_RUNNING(self):
        """Message constant 'TROT_RUNNING'."""
        return Metaclass_SetGait_Request.__constants['TROT_RUNNING']

    @property
    def CLIMB_STAIRS(self):
        """Message constant 'CLIMB_STAIRS'."""
        return Metaclass_SetGait_Request.__constants['CLIMB_STAIRS']

    @property
    def TROT_OBSTACLE(self):
        """Message constant 'TROT_OBSTACLE'."""
        return Metaclass_SetGait_Request.__constants['TROT_OBSTACLE']


class SetGait_Request(metaclass=Metaclass_SetGait_Request):
    """
    Message class 'SetGait_Request'.

    Constants:
      IDLE
      TROT
      TROT_RUNNING
      CLIMB_STAIRS
      TROT_OBSTACLE
    """

    __slots__ = [
        '_gait',
    ]

    _fields_and_field_types = {
        'gait': 'uint8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.gait = kwargs.get('gait', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.gait != other.gait:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def gait(self):
        """Message field 'gait'."""
        return self._gait

    @gait.setter
    def gait(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'gait' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'gait' field must be an unsigned integer in [0, 255]"
        self._gait = value


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_SetGait_Response(type):
    """Metaclass of message 'SetGait_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('unitree_nav_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'unitree_nav_interfaces.srv.SetGait_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_gait__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_gait__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_gait__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_gait__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_gait__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SetGait_Response(metaclass=Metaclass_SetGait_Response):
    """Message class 'SetGait_Response'."""

    __slots__ = [
    ]

    _fields_and_field_types = {
    }

    SLOT_TYPES = (
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)


class Metaclass_SetGait(type):
    """Metaclass of service 'SetGait'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('unitree_nav_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'unitree_nav_interfaces.srv.SetGait')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__set_gait

            from unitree_nav_interfaces.srv import _set_gait
            if _set_gait.Metaclass_SetGait_Request._TYPE_SUPPORT is None:
                _set_gait.Metaclass_SetGait_Request.__import_type_support__()
            if _set_gait.Metaclass_SetGait_Response._TYPE_SUPPORT is None:
                _set_gait.Metaclass_SetGait_Response.__import_type_support__()


class SetGait(metaclass=Metaclass_SetGait):
    from unitree_nav_interfaces.srv._set_gait import SetGait_Request as Request
    from unitree_nav_interfaces.srv._set_gait import SetGait_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
