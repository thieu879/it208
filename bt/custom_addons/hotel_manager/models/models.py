from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
from datetime import timedelta


class HotelRoomType(models.Model):
	_name = 'hotel.room.type'
	_description = 'Loại phòng'

	name = fields.Char(string='Tên loại', required=True)
	code = fields.Char(string='Mã loại')


class HotelService(models.Model):
	_name = 'hotel.service'
	_description = 'Dịch vụ đi kèm'

	name = fields.Char(string='Tên dịch vụ', required=True)
	price = fields.Integer(string='Giá dịch vụ', required=True)

	_sql_constraints = [
		('service_price_positive', 'CHECK(price > 0)', 'Giá dịch vụ phải lớn hơn 0!'),
	]


class HotelCustomer(models.Model):
	_name = 'hotel.customer'
	_description = 'Khách hàng'
	_order = 'name'

	name = fields.Char(string='Tên khách', required=True)
	identity_card = fields.Char(string='Số CMND/CCCD')
	phone = fields.Char(string='Số điện thoại')

	_sql_constraints = [
		('identity_card_unique', 'UNIQUE(identity_card)', 'Số CMND/CCCD phải duy nhất!'),
	]


class HotelRoom(models.Model):
	_name = 'hotel.room'
	_description = 'Phòng khách sạn'

	name = fields.Char(string='Số phòng', required=True)
	floor = fields.Integer(string='Tầng')
	price_per_night = fields.Integer(string='Giá / đêm', required=True)
	status = fields.Selection([
		('available', 'Trống'),
		('occupied', 'Đang ở'),
		('maintenance', 'Bảo trì')
	], string='Trạng thái', default='available')

	type_id = fields.Many2one('hotel.room.type', string='Loại phòng')

	_sql_constraints = [
		('room_name_unique', 'UNIQUE(name)', 'Tên phòng phải duy nhất!'),
		('room_price_positive', 'CHECK(price_per_night > 0)', 'Giá phòng phải lớn hơn 0!'),
	]


class HotelBooking(models.Model):
	_name = 'hotel.booking'
	_description = 'Phiếu Đặt phòng'

	code = fields.Char(string='Mã booking')
	customer_id = fields.Many2one('hotel.customer', string='Khách hàng')
	room_id = fields.Many2one('hotel.room', string='Phòng')
	check_in = fields.Date(string='Check-in', default=fields.Date.context_today)
	check_out = fields.Date(string='Check-out')
	duration = fields.Integer(string='Số đêm', compute='_compute_duration', store=True)
	service_ids = fields.Many2many('hotel.service', string='Dịch vụ thêm')
	total_amount = fields.Integer(string='Tổng tiền', compute='_compute_total_amount', store=True)
	state = fields.Selection([
		('draft', 'Nháp'),
		('confirmed', 'Đã xác nhận'),
		('done', 'Hoàn thành')
	], string='Trạng thái', default='draft')

	@api.depends('check_in', 'check_out')
	def _compute_duration(self):
		for rec in self:
			if rec.check_in and rec.check_out:
				d_in = fields.Date.from_string(rec.check_in)
				d_out = fields.Date.from_string(rec.check_out)
				rec.duration = (d_out - d_in).days if d_out and d_in else 0
			else:
				rec.duration = 0

	@api.depends('room_id', 'duration', 'service_ids')
	def _compute_total_amount(self):
		for rec in self:
			room_total = 0
			services_total = 0
			if rec.room_id and rec.duration:
				room_total = rec.room_id.price_per_night * rec.duration
			if rec.service_ids:
				services_total = sum(service.price for service in rec.service_ids)
			rec.total_amount = room_total + services_total

	@api.onchange('room_id')
	def _onchange_room_id(self):
		if self.room_id and self.room_id.status == 'maintenance':
			return {
				'warning': {
					'title': 'Phòng đang bảo trì',
					'message': 'Phòng này đang bảo trì, vui lòng chọn phòng khác!'
				}
			}

	@api.onchange('check_in')
	def _onchange_check_in(self):
		if self.check_in:
			d_in = fields.Date.from_string(self.check_in)
			d_out = d_in + timedelta(days=1)
			self.check_out = fields.Date.to_string(d_out)

	@api.constrains('check_in', 'check_out')
	def _check_dates(self):
		for rec in self:
			if rec.check_in and rec.check_out:
				d_in = fields.Date.from_string(rec.check_in)
				d_out = fields.Date.from_string(rec.check_out)
				if d_out <= d_in:
					raise ValidationError('Ngày trả phòng không hợp lệ!')

	@api.constrains('room_id')
	def _check_room_not_occupied(self):
		for rec in self:
			if rec.room_id and rec.room_id.status == 'occupied':
				raise ValidationError('Phòng này đang có khách ở!')

