""":mod:`wand.cdefs.structures` --- MagickWand C-Structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 0.5.0
"""
from ctypes import POINTER, Structure, c_double, c_int, c_size_t
from wand.cdefs.wandtypes import c_ssize_t, c_magick_real_t, c_magick_size_t

__all__ = ('AffineMatrix', 'ChannelFeature', 'GeomertyInfo', 'KernelInfo',
           'MagickPixelPacket', 'PixelInfo', 'PointInfo', 'RectangleInfo')


class AffineMatrix(Structure):

    _fields_ = [('sx', c_double),
                ('rx', c_double),
                ('ry', c_double),
                ('sy', c_double),
                ('tx', c_double),
                ('ty', c_double)]


class ChannelFeature(Structure):
    """
    /*
      Haralick texture features.
    */
    typedef struct _ChannelFeatures
    {
      double
        angular_second_moment[4],
        contrast[4],
        correlation[4],
        variance_sum_of_squares[4],
        inverse_difference_moment[4],
        sum_average[4],
        sum_variance[4],
        sum_entropy[4],
        entropy[4],
        difference_variance[4],
        difference_entropy[4],
        measure_of_correlation_1[4],
        measure_of_correlation_2[4],
        maximum_correlation_coefficient[4];
    } ChannelFeatures;
    """
    _fields_ = [('angular_second_moment', c_double * 4),
                ('contrast', c_double * 4),
                ('correlation', c_double * 4),
                ('variance_sum_of_squares', c_double * 4),
                ('inverse_difference_moment', c_double * 4),
                ('sum_average', c_double * 4),
                ('sum_variance', c_double * 4),
                ('sum_entropy', c_double * 4),
                ('entropy', c_double * 4),
                ('difference_variance', c_double * 4),
                ('difference_entropy', c_double * 4),
                ('measure_of_correlation_1', c_double * 4),
                ('measure_of_correlation_2', c_double * 4),
                ('maximum_correlation_coefficient', c_double * 4)]


class GeomertyInfo(Structure):

    _fields_ = [('rho', c_double),
                ('sigma', c_double),
                ('xi', c_double),
                ('psi', c_double),
                ('chi', c_double)]


class KernelInfo(Structure):
    pass


KernelInfo._fields_ = [('type', c_int),
                       ('width', c_size_t),
                       ('height', c_size_t),
                       ('x', c_ssize_t),
                       ('y', c_ssize_t),
                       ('values', POINTER(c_double)),
                       ('minimum', c_double),
                       ('maximum', c_double),
                       ('negative_range', c_double),
                       ('positive_range', c_double),
                       ('angle', c_double),
                       ('next', POINTER(KernelInfo)),
                       ('signature', c_size_t)]


class MagickPixelPacket(Structure):

    _fields_ = [('storage_class', c_int),
                ('colorspace', c_int),
                ('matte', c_int),
                ('fuzz', c_double),
                ('depth', c_size_t),
                ('red', c_magick_real_t),
                ('green', c_magick_real_t),
                ('blue', c_magick_real_t),
                ('opacity', c_magick_real_t),
                ('index', c_magick_real_t)]


class OffsetInfo(Structure):

    _fields_ = [('x', c_double),
                ('y', c_double)]


class PixelInfo(Structure):

    _fields_ = [('storage_class', c_int),
                ('colorspace', c_int),
                ('alpha_trait', c_int),
                ('fuzz', c_double),
                ('depth', c_size_t),
                ('count', c_magick_size_t),
                ('red', c_magick_real_t),
                ('green', c_magick_real_t),
                ('blue', c_magick_real_t),
                ('black', c_magick_real_t),
                ('alpha', c_magick_real_t),
                ('index', c_magick_real_t)]


class PointInfo(Structure):

    _fields_ = [('x', c_double),
                ('y', c_double)]


class RectangleInfo(Structure):

    _fields_ = [('width', c_size_t),
                ('height', c_size_t),
                ('x', c_ssize_t),
                ('y', c_ssize_t)]


class CCObjectInfo(Structure):
    _fields_ = [('_id', c_ssize_t),
                ('bounding_box', RectangleInfo),
                ('color', PixelInfo),
                ('centroid', PointInfo),
                ('area', c_double),
                ('census', c_double)]


# All this will change with IM7, so let's not implement this just yet.
#
# class ImageChannelStatistics(Structure):
#     _fields_ = [('maximum', c_double),
#                 ('minimum', c_double),
#                 ('mean', c_double),
#                 ('standard_deviation', c_double),
#                 ('variance', c_double),
#                 ('kurtosis', c_double),
#                 ('skewness', c_double)]
#
# class ImageStatistics(Structure):
#     _fields_ = [('red', ImageChannelStatistics),
#                 ('green', ImageChannelStatistics),
#                 ('blue', ImageChannelStatistics),
#                 ('opacity', ImageChannelStatistics)]
